from redis import Redis
import logging

logging.basicConfig(level=logging.INFO)
redis = Redis(host='myfirstredisdatabase.dzygwu.0001.euc1.cache.amazonaws.com', port=6379, decode_responses=True, ssl=True, username='root', password='merda77$')

if redis.ping():
    logging.info("Connected to Redis")