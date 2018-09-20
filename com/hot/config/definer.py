from tornado.options import define, options

define("DB_HOST", default="127.0.0.1", help="db host", type=str)
define("DB_USER", default="root", help="db user", type=str)
define("DB_PASS", default="rrg88888", help="db password", type=str)
define("DB_NAME", default="robcoupon", help="db name", type=str)


define("REDIS_HOST", default="127.0.0.1", help="redis host", type=str)
define("REDIS_PORT", default=6379, help="redis port", type=int)
define("REDIS_PW", default="rrg88888", help="redis password", type=str)
define("REDIS_KEY_PREFIX", default="rob_coupon_", help="redis all key's prefix", type=str)


define("TOKEN_EXPIRE", default=300, help="token expire time (second)", type=int)
