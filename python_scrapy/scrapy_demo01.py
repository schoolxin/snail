# -*- coding:utf-8 -*-
# @FileName  :scrapy_demo01.py
# @Time      :2023/10/5 9:48
# @Author    :dzz
# @Function  :
# http://www.woniunote.com/  蜗牛笔记
from urllib.parse import urljoin

import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import csv

content_list = []


# 详情页面
def parse_note_page_detail(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    title = html.xpath("//div[contains(@class,'title')]")[0].text.strip()
    # print(title)
    info = soup.find_all(attrs={'class': 'info'})[0].get_text().strip()
    # print(info)
    author = re.findall("作者：(.*?)\s+", info, re.S)[0]
    # print(author)
    category = re.findall("类别：(.*?)\s+", info, re.S)[0]
    # print(category)
    date = re.findall("日期：(.*?)\s+", info, re.S)[0]
    # print(date)
    read_cnts = re.findall("阅读：(.*?)\s+", info, re.S)[0]
    # print(read_cnts)
    consumption_points = re.findall("消耗积分：(.*?)\s+", info, re.S)[0]
    # print(consumption_points)
    # print(soup.find_all(attrs={'class': 'title'})[0].get_text().strip())
    # 获取内容
    # content = html.xpath("//div[@id='content']")[0].xpath("string(.)").strip()
    content = soup.find_all(attrs={'id': 'content'})[0].get_text().strip()
    # print(content)
    # 获取图片 <img src="https://woniuxyopenfile.oss-cn-beijing.aliyuncs.com/woniuxynote/image/201805/20180529_112119_384.jpg">
    images = re.findall('<img src="(https://woniuxyopenfile.oss-cn-beijing.aliyuncs.com/woniuxynote/image/.*?)".*?>',
                        resp.text, re.S)
    # print(images, type(images))
    content_list.append([url, title, author, category, date, read_cnts, consumption_points, images])


print("列表页解析")


def parse_note_list(page):
    list_url = "http://www.woniunote.com/page/{}".format(page)
    print("正在处理第{}页url地址为{}".format(page, list_url))
    resp_list = requests.get(list_url)
    xpath_list = etree.HTML(resp_list.text)
    soup_list = BeautifulSoup(resp_list.text, 'lxml')
    list_pages = xpath_list.xpath("//div[@class='title']//a")
    for list_page in list_pages:
        yield urljoin("http://www.woniunote.com", list_page.get('href'))


if __name__ == "__main__":

    for i in range(1, 11):
        for page in parse_note_list(i):
            parse_note_page_detail(page)
    # print(content_list)
    with open('woniunote.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(['文章地址', '标题', '作者', '类型', '日期', '阅读数', '消耗积分', '图片链接'])
        for p in content_list:
            writer.writerow(p)
    print("处理完成")
