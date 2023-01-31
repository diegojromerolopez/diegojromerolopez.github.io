---
title: Dockerfile stages must have a command
date: "2023-01-31T00:00:00+01:00"
draft: false
tags: ["docker"]
---

# Dockerfile stages must have a command
In multi-stage Dockerfile, you have to be careful
for what stages you run. Want to avoid having
misteriously exit 0 errors in containers?
Add a CMD at the end of the Dockerfile stage
with some dummy command like

```Dockerfile
CMD ["/bin/bash", "echo", "Command for stage X"]
```

Any stage that has no command will exit without
informing the user of what happened. This could
cause some *mysterious* errors if you are getting
up all containers and not overwritting the command
of the ones that have none.

## Conclusion
A good way of making sure you are not exiting
early while being oblivious of what is happening
is setting a dummy command for each stage in a
multi-stage Dockerfile.
