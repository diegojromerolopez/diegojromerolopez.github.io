---
title: Immutability
date: "2021-06-06T00:00:00+00:00"
draft: false
tags: ["immutability", "python", "project"]
---

# Introduction
In this post I will explain the rationale about working with immutable objects
and will present a personal project I've been working on the last few days:
[Gelidum](https://github.com/diegojromerolopez/gelidum).

![La Nevada, painted by Francisco de Goya](/static/images/la-nevada.jpeg "La Nevada by Francisco de Goya")

# Introducing Gelidum
[Gelidum](https://github.com/diegojromerolopez/gelidum) (pronounced *ye-lee-doom*,
meaning *frozen* in latin) is a [python package](https://pypi.org/project/gelidum/)
that allows you to freeze and object (and all of its references), making it immutable.
What does it mean to be immutable? All attributes of this object cannot have their values
changed. Further, this *freezing* is a **deep** freeze, meaning that all the attributes
that are objects will also be frozen, and the attributes of each of this attributes and
so on. Any object referenced by this object or one of its descendents will be frozen.

# How did you do this?
The idea of Gelidum is remove all attributes that can modify the current attributes of an
instance or that can add new attributes.

The core of this project is [a function that creates a frozen-version of a class](https://github.com/diegojromerolopez/gelidum/blob/main/gelidum/frozen.py).
This froze-version has all setting-attr
([\_\_setattr\_\_](https://docs.python.org/3/reference/datamodel.html#object.__setattr__),
[\_\_set\_\_](https://docs.python.org/3/reference/datamodel.html#object.__set__),
[\_\_delattr\_\_](https://docs.python.org/3/reference/datamodel.html#object.__delattr__),
[\_\_setitem\_\_](https://docs.python.org/3/reference/datamodel.html#object.__setitem__),
[\_\_delitem\_\_](https://docs.python.org/3/reference/datamodel.html#object.__delitem__),
[\_\_reversed\_\_](https://docs.python.org/3/reference/datamodel.html#object.__reversed__)) methods overwritten by an exception-raising method.

It also has an empty [\_\_slots\_\_](https://docs.python.org/3/reference/datamodel.html#slots) class-attribute to avoid adding new attributes.

And finally, it overwrites the contents of writtable attributes (i.e. the [\_\_dict\_\_](https://docs.python.org/3/library/stdtypes.html#object.__dict__) dictionary) by assigning None to their values, making them unwrittable, and hence forcing the developer to access the
attributes directly.

```python
class FrozenBase(object):
    def __setattr__(self, key, value):
        raise FrozenException(f"Can't assign '{key}' on immutable instance")

    def __set__(self, *args, **kwargs):
        raise FrozenException("Can't assign setter on immutable instance")

    def __delattr__(self, name):
        raise FrozenException(
            f"Can't delete attribute '{name}' on immutable instance")

    def __setitem__(self, key, value):
        raise FrozenException("Can't set key on immutable instance")

    def __delitem__(self, key):
        raise FrozenException("Can't delete key on immutable instance")

    def __reversed__(self):
        raise FrozenException("Can't reverse on immutable instance")


def make_frozen_class(klass: Type[object], attrs: List[str]):
    frozen_class = type(
        f"Frozen{klass.__name__}",
        (klass, FrozenBase),
        {
            "__slots__": tuple(),
            **{attr: None for attr in attrs}
        }
    )
    return frozen_class
```

When calling from the
[freeze function](https://github.com/diegojromerolopez/gelidum/blob/main/gelidum/freeze.py),
a mutual recursive function is called, calling the version of
freeze for the class of each one of its attributes. The base cases of the recursive function call are the following ones:
- object is builtin type: return the object, no change is needed.
- object is bytearray: return a bytes copy.

```python
def freeze(obj: Any, inplace: bool = False) -> Any:
    if isbuiltin(obj):
        return obj

    class_name = type(obj).__name__
    freeze_func_name = f"__freeze_{class_name}"
    this_module = sys.modules[__name__]
    if hasattr(this_module, freeze_func_name):
        freeze_func = getattr(this_module, freeze_func_name)
        return freeze_func(obj, inplace=inplace)

    if isinstance(obj, object):
        return __freeze_object(obj, inplace=inplace)

    raise ValueError(f"object of type {obj.__class__} not frozen")
```

You may have seen the **inplace** parameter, having it with a True value
will make to freeze the current objects when possible (e.g. builtin objects
cannot be frozen). Passing a False value (its default value) will make
frozen copies instead.

# How to use it
Using gelidum is very easy, import the method freeze and call the object
you want to make immutable:

```python
from gelidum import freeze

my_frozen_object = freeze(my_object, inplace=True)
assert id(my_frozen_object) == id(my_object)

my_frozen_copy = freeze(my_object, inplace=False)
assert id(my_frozen_copy) != id(my_object)
```

Remember, as you can see above, you can freeze your object
in the same object (if possible), or freeze your object
in a new copy. Asserts are added to make it clearer.

If you want to check other examples, please see the
[tests of this freze function](https://github.com/diegojromerolopez/gelidum/blob/main/tests/gelidum_tests/test_freeze.py) where you can see different use-cases.

There is also a decorator to freeze input params. But at the moment is a bit
limited as all \*args attributes will be frozen and you can only choose what
\*\*kwargs attributes are frozen by passing the names of that attributes in
the params input parameter.

# Why did you do this?
Well, having worked with Ruby in the past, I loved how the objects have
a freeze method and, although, its intended use was to make strings and
constants immutable, it inspired me to expand the concept to any object
and with a deep-freeze. However, I did it Python as you can see as is
my current to-go programming language nowadays.

# Is it safe?
There are some tests in the package but I have classified this package
as alpha. I have not tested in production environments with concurrency and
parallelism, so there is no warranty of working 100% fine.

Thus, I have tested with the CPython interpreter, I have not checked it with
pypy, although it should be working perfectly as this module is pure-python.

However, if you find a bug, feel free to open an issue in the project's
page and will take a look at it as soon as possible.

# Conclusion
This post shows a project with the intent of making immutable objects (*freezing objects*)
more easier. Its current release is alpha but all use-cases that have been tested
have been successful.

If you want to work this package, or find any bug, create an issue and I will take a look
without any doubt.