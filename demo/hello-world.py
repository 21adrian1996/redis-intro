#!/usr/bin/env python

import redis
r = redis.Redis()
r.set("msg:hello", "Hello Redis!!!")
msg = r.get("msg:hello")
print(msg)
