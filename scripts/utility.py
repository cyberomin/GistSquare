import redis
import time

r = redis.Redis()

r.set("user:1","Joe")
r.set("post:1","This is it. I'm loving redis")

r.sadd("user:1:posts",2)
print r.smembers("user:1:posts")