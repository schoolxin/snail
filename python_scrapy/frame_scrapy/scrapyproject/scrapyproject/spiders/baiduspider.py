import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = "baiduspider"
    allowed_domains = ["www.baidu.com"]
    # start_urls = ["https://www.baidu.com"]

    # 默认生成的parse 专门作为start_urls 里面的url的response回调方法
    def parse(self, response):
        # self.logger.info(response.text)
        self.logger.debug(response.status)
    def start_requests(self):

        yield scrapy.Request(url="https://www.baidu.com",callback=self.parse)
