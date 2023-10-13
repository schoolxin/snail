import re

import scrapy

from ..items import PiplinedemoItem


class WoniunoteSpider(scrapy.Spider):
    name = "woniunote"
    allowed_domains = ["www.woniunote.com"]

    # start_urls = ["http://www.woniunote.com"]

    def start_requests(self):
        base_url = "https://www.woniuxy.com/note/page-{}"

        for page in range(1, 11):
            url = base_url.format(str(page))
            # 直接把带请求的地址扔到scrapy的请求队列中  dont_filter=True 不要让scrapy 自动过滤掉相似的请求
            yield scrapy.Request(url=url, callback=self.parse_list, dont_filter=True)

    def parse(self, response):
        pass

    def parse_list(self, response):
        # content_url = response.xpath("//div[@class='title']/a/@href").extract()
        content_url = response.xpath("//div[@id='content']/a/@href").getall()
        # print("content_url", content_url)
        for url in content_url:
            # print(response.urljoin(url))
            yield scrapy.Request(url=response.urljoin(url),
                                 callback=self.parse_content,
                                 dont_filter=True
                                 )

    def parse_content(self, response):

        items = PiplinedemoItem()
        items['title'] = response.xpath("//h1[@class='content-title']/text()").extract()[0].strip()


        items['date'] = response.xpath("//p[@class='date-year']/text()").extract()[0].strip() + "/" + \
                        response.xpath("//p[@class='date-time']/text()").extract()[0].strip()

        items['read'] = 0


        return items
