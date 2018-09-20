import redis
from com.hot.config.definer import *


class RedisManager:
    def __init__(self):
        self.pool = redis.ConnectionPool(host=options.REDIS_HOST, port=options.REDIS_PORT, password=options.REDIS_PW)

    def get_conn(self):
        return redis.Redis(connection_pool=self.pool)


_redis_manager = RedisManager()


class RedisClient:
    @staticmethod
    def set(name, value, ex=None, px=None, nx=False, xx=False):
        name = options.REDIS_KEY_PREFIX + name
        _redis_manager.get_conn().set(name, value, ex=ex, px=px, nx=nx, xx=xx)

    @staticmethod
    def get(name):
        name = options.REDIS_KEY_PREFIX + name
        return _redis_manager.get_conn().get(name)





# if __name__ == '__main__':
    # redis_cli = _redis_manager.get_conn()
    # redis_cli.set("k1", "123",ex=10)
    # res = redis_cli.get('k1')
    # print(res)
