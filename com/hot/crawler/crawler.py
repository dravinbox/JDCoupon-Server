from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class Crawler:

    def __init__(self, target='https://a.jd.com/'):
        self.page_offset = 1000
        self.driver = webdriver.Chrome()
        self.driver.get(target)
        self.js_script = "window.scrollTo(0,document.body.scrollHeight-1000)"

        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector('div.loading'))
        except TimeoutException:
            return
        else:
            self.my_ini()

    def my_ini(self):
        while True:
            try:
                self.driver.find_element_by_css_selector('div.loading')
            except NoSuchElementException:
                break
            except StaleElementReferenceException:
                print("============div.loding 不存在了==================")
                break

            else:
                print("============div.loading==================")
                self.driver.execute_script(self.js_script)
                try:
                    WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_css_selector('div.loading'))
                except TimeoutException:
                    break

    def get_key_arr(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        txt = soup.select("div.quan-item > div.q-type > div.q-range > span")
        arr = []
        for i in range(len(txt)):
            # print(txt[i].text)
            if '手机' in txt[i].text:
                print(txt[i].text)
                tmp = soup.select("div.quan-item > div.q-ops-box > div.q-opbtns > a")[i].get_attribute_list('rel')
                if tmp[0] is None:
                    continue
                else:
                    arr.append(tmp[0])

        # res = soup.select("a[rel]")
        # arr = []
        # for r in res:
        #     tmp = r.get_attribute_list('rel')
        #     if tmp.__len__() <= 0 or tmp[0] == 'nofollow':
        #         continue
        #     else:
        #         arr.append(tmp[0])

        print(arr)
        return arr

        # req = requests.get(url=target)
        # html = req.text
        # bf = BeautifulSoup(html, "html.parser")
        # texts = bf.findAll('div', class_='quan-item')

        # return str(r)
