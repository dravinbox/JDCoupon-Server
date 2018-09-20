import tornado.web
from com.hot.service.services import *
from com.hot.config.result import Result
from com.hot.config.redis_api import RedisClient
from com.hot.tool.util import TokenGenerator
from com.hot.config.definer import *


class LoginHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        phone = self.get_body_argument("phone")
        password = self.get_body_argument("password")
        user_service = UserService()
        res = user_service.vertify_user_by_phone_and_pw(phone, password)
        if res is None:
            self.write(Result.failure_with_msg("登录失败"))
        else:
            token = TokenGenerator.get_token()
            RedisClient.set("user_id_"+str(res['user_id']), token, ex=options.TOKEN_EXPIRE, nx=True)
            res['token'] = token
            self.write(Result.success(res))


class UserInfoHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("user info")

    def post(self, *args, **kwargs):
        self.write("post user info")
