---
title: The testing pyramid
date: "2025-06-07T00:00:00+02:00"
draft: false
tags: ["software", "testing"]
---

# The test pyramid
This post revisit one of my favorite topics: [testing](/tags/testing/).
We are going to delve into what are the different types of tests that you should do in your software
to have some assurance about your code.

## Introduction
I wrote some time ago a post about the
[difference between unit and integration testing](/blog/2022/11/actual-integration-tests/),
and while re-reading it today I was not convinced that it was clear enough.

*Integration tests* is a concept that has been used many times in different environments and at different
levels, so I want to give a proper definition of each one of the test types at project and system level. 

## Working example

Along this post I will use this toy example as a mean to show how to implement the different type of tests.

This example is just two different health service modules for two redis cache servers: AI and users.

Both call to a common redis health checker module.

```python
from logging import Logger
from services.health import redis_is_healthy

# services/health/user_cache.py
def user_cache_is_healthy(logger: Logger) -> bool:
    healthy = redis_is_healthy(host='user.cache.cluster', port=6379)
    if healthy:
        logger.debug('The user cache is healthy')
    else:
        logger.error('The user cache is not healthy')
    return healthy
```

```python
# services/health/redis.py
from redis import Redis
from redis.exceptions import RedisError

def redis_is_healthy(host: str, port: int, db: int = 0) -> bool:
     redis = Redis(host=host, port=port, db=db)

    try:
        response = redis.ping()
        if response:
            return True
        return False
    except RedisError as exc:
        return False
```


## Unit tests
I wrote about [unit testing recently](/blog/2025/04/how-to-write-a-good-unit-test/), and the point of that post stands:
**unit tests are tests than only check the contract with the immediate layer below**.

These tests are implemented at project-level.

So if you have a function that calls a service that does other calls, to test the function
you would need to mock the service and assume its behavior to be correct.

For the user cache health checker the unit tests would be the following ones:

```python
from unittest import TestCase
from unittest.mock import MagicMock, patch, call


@patch('services.health.user_cache.redis_is_healthy')
class TestUserCacheHealth(TestCase):
    def test_healthy(self, mock_redis_is_healthy: MagicMock):
        mock_redis_is_healthy.return_value = True
        mock_logger = MagicMock()
        
        mock_requests_get.return_value = MagicMock(status_code=200)
        
        healthy = user_cache_is_healthy(logger=mock_logger)

        self.assertTrue(healthy)
        self.assertEqual([call(host='user.cache.cluster', port=6379)], mock_redis_is_healthy.call_args_list)
        self.assertEqual([call('The user cache is healthy')], mock_logger.debug.call_args_list)
        self.assertEqual([], mock_logger.error.call_args_list)

    def test_unhealthy(self, mock_redis_is_healthy: MagicMock):
        mock_redis_is_healthy.return_value = False
        mock_logger = MagicMock()
        
        mock_requests_get.return_value = MagicMock(status_code=200)
        
        healthy = user_cache_is_healthy(logger=mock_logger)

        self.assertFalse(healthy)
        self.assertEqual([call(host='user.cache.cluster', port=6379)], mock_redis_is_healthy.call_args_list)
        self.assertEqual([], mock_logger.debug.call_args_list)
        self.assertEqual([call('The user cache is not healthy')], mock_logger.error.call_args_list)
```

As you see in the code above, the tests are mocking the immediate called modules. In this example, the
only loaded dependencies are the `services.health.redis_is_healthy` function and the logger input parameter.

## Integration tests
While in the [Actual Integration Tests](/blog/2022/11/actual-integration-tests/)
I said that the integration tests do not mock anything,
that is wrong. I would say that is true for the system integration tests, but mostly, when we
say *integration tests* we are talking about a lone project, and we mean *software component integration tests*.

Following this principle, the integration tests are implemented at project-level.

So, it does not make sense to test all components with integration tests, usually only the most external interfaces
of a system need to be checked. For example, if we are developing an API, we should only do integration tests
on the API component.

Having said that, we could improve the definition a bit:

**integration tests are tests that need to mock only the lowest level possible (typically just I/O) and test fully a component**.

For the user cache health checker the integration tests would be the following ones:

```python
from unittest import TestCase
from unittest.mock import MagicMock, patch, call


@patch('services.health.redis.Redis')
class TestUserCacheHealth(TestCase):
    def test_healthy(self, mock_redis_class: MagicMock):
        mock_redis = MagicMock()
        mock_redis.ping.return_value = True
        mock_redis_class.return_value = mock_redis
        
        mock_logger = MagicMock()
        
        mock_requests_get.return_value = MagicMock(status_code=200)
        
        healthy = user_cache_is_healthy(logger=mock_logger)

        self.assertTrue(healthy)
        self.assertEqual([call(host='user.cache.cluster', port=6379, db=0)], mock_redis_class.call_args_list)
        self.assertEqual([call()], mock_redis.ping.call_args_list)
        self.assertEqual([call('The user cache is healthy')], mock_logger.debug.call_args_list)
        self.assertEqual([], mock_logger.error.call_args_list)

    def test_unhealthy(self, mock_redis_class: MagicMock):
        mock_redis = MagicMock()
        mock_redis.ping.return_value = False
        mock_redis_class.return_value = mock_redis

        mock_logger = MagicMock()
        
        mock_requests_get.return_value = MagicMock(status_code=200)
        
        healthy = user_cache_is_healthy(logger=mock_logger)

        self.assertFalse(healthy)
        self.assertEqual([call(host='user.cache.cluster', port=6379, db=0)], mock_redis_class.call_args_list)
        self.assertEqual([call()], mock_redis.ping.call_args_list)
        self.assertEqual([], mock_logger.debug.call_args_list)
        self.assertEqual([call('The user cache is not healthy')], mock_logger.error.call_args_list)
```

As you see in these tests, what is mocking is not the immediate called dependencies, but the lowest level possible.
In our case, lowest level dependency it the redis library. That library (an external dependency) is the one that
should be mocked.

We assume all the intermediate logic will work fine, and we only check the communication with external systems.

## End to end tests
This kind of tests are those that I refer before as *system integration*.

You could argue that when we have a pure function its unit tests can be considered end to end tests,
but the thing is that the end to end not only do not mock anything, but they are meant to test
systems. So we can improve the definition by saying:

**The end to end tests are tests where nothing is mocked and we check the behavior of a system**.

The system usually is an application, or a collection of applications (depending of the complexity of the
test).

Take in account that most of the times you would need to mock some data sources or services, because it makes testing easier,
even though the test would not be a *pure* end-to-end test, but useful for your purposes.
Creating **services that return mocked data** instead of actual data it is a good strategy to test specific scenarios.

These tests are not done inside the project, I mean, they are not coded as the other tests. In my experience, that is usually
done by deploying the applications in a testing environment and interacting with them and checking the results.

## Bonus: What are smoke tests?
End to end tests that are critical to signal if there is a broken feature. I think the name *smoke tests* comes
from the term *smoking gun* (main evidence that solves a crime). In this case it is meant to be a type of tests
that ensure that the critical features work.

## Conclusion
I hope I have amended some inconsistencies and inexactitudes of other posts.
Do you create all these tests when development a new project?
