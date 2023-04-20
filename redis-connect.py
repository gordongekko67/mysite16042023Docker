import redis

pool = redis.ConnectionPool(host='demo-redis.5og6vn.ng.0001.euc1.cache.amazonaws.com', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)

redis.set('mykey', 'Hello from Python!')
value = redis.get('mykey')
print(value)

redis.zadd('vehicles', {'car' : 0})
redis.zadd('vehicles', {'bike' : 0})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)