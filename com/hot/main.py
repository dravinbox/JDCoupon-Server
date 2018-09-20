#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from com.hot.comm_log import *
from com.hot.coupon.coupon import *
from com.hot.crawler.crawler import *
from com.hot.controller.user_handler import *
import subprocess
import json
import re
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

# test
# 监听端口
define("port", default=9090, help="run on the given port", type=int)
# 日志输出
define("log", default=get_logging('dj_coupon'))


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print('input_url=====:'+self.get_argument('url'))
        crawler = Crawler(self.get_argument('url'))
        key_arr = crawler.get_key_arr()
        print(key_arr)
        self.write("查到有关 '<font color='red'>手机</font> '字的有"+str(len(key_arr))+"张券")
        # if len(key_arr) > 0:
        #     couponer = Coupon()
        #     couponer.set_request_urls_with_keys_arr(key_arr)
        #     couponer.get_coupon()

    def post(self):
        self.write('post done.')


application = tornado.web.Application([
    (r"/test", MainHandler),
    (r"/user/login", LoginHandler),
    (r"/user/info", UserInfoHandler),
])


if __name__ == "__main__":
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

