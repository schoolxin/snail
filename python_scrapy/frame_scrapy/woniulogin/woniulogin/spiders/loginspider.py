import json

import scrapy


# https://woniuxy.com/sys/user/login
# https://woniuxy.com/sys/user/captcha?t=Math.random()
class LoginspiderSpider(scrapy.Spider):
    name = "loginspider"
    allowed_domains = ["www.woniuxy.com"]
    start_urls = ["https://www.woniuxy.com"]



    def getCaptcha(self, response):

        with open('checkcode.png', 'wb') as file:
            file.write(response.body)
        code = str(input("请输入验证码"))
        data = {
            'tel': response.meta['tel'],
            'password': response.meta['password'],
            'captcha': code,
            'loginType': str(response.meta['loginType'])
        }
        # print(data)
        return [scrapy.FormRequest(url='https://woniuxy.com/sys/user/login',formdata=data,callback=self.after_login,dont_filter=True)]  # post 请求

    def start_requests(self):
        return [scrapy.Request(
            url='https://woniuxy.com/sys/user/captcha?t=Math.random()',
            meta={"tel": "15591819289", "password": "708170", "loginType": 1},
            callback=self.getCaptcha
        )]

    def after_login(self, response):
        print("hhhh")
        self.logger.debug(response.text)

