import requests
import time
import random
import json


# 将cookie转为字典
def get_cookie():
    with open("./coupon/cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies


class Coupon:
    session = requests.session()
    scheduled_time = "2018-09-15 09:17"
    # 券的URL
    requestUrls = []
    # 券的Refer
    referer = "https://a.jd.com/"
    # 浏览器及版本
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"

    def __init__(self):
        self.session.headers['User-Agent'] = self.user_agent
        self.session.cookies = requests.utils.cookiejar_from_dict(get_cookie())

    def get_coupon(self):
        for i in range(len(self.requestUrls)):
            self.session.headers['Referer'] = self.referer
            r = self.session.get(self.requestUrls[i])
            json_str = json.loads(str(r.text)[13:-1])
            print("===1==="+r.text)
            if json_str['message'] == '抢得太快了，臣妾做不到啊~':
                self.re_try(self.requestUrls[i], 3)
                continue
            time.sleep(3)

    def re_try(self, url, t=3):
        time.sleep(t)
        self.session.headers['Referer'] = self.referer
        r = self.session.get(url)
        print("==="+str(t)+"==="+r.text)
        json_str = json.loads(str(r.text)[13:-1])
        if json_str['message'] == '抢得太快了，臣妾做不到啊~':
            self.re_try(url, t+3)
        else:
            return

    def set_request_urls_with_keys_arr(self, arr):
        for a in arr:
            url = "https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery"+self.random_number(6)+"&key="+a+"&type=1&_="+str(round(time.time()*1000))
            print(url)
            self.requestUrls.append(url)

    def set_request_urls(self, arr):
        self.requestUrls = arr

    def add_request_url(self, url):
        self.requestUrls.append(url)

    def get_request_urls(self):
        return self.requestUrls

    def random_number(self,n):
        return ''.join(str(i) for i in random.sample(range(0, 9), n))
