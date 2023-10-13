import scrapy


class UaspiderSpider(scrapy.Spider):
    name = "uaspider"
    allowed_domains = ["web"]
    start_urls = ["https://www.httpbin.org/user-agent"]

    def parse(self, response):
        self.logger.debug(response.text)
