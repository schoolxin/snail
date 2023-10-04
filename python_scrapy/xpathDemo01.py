# -*- coding:utf-8 -*-
# @FileName  :xpathDemo01.py
# @Time      :2023/10/4 10:38
# @Author    :dzz
# @Function  :
from lxml import etree
import requests

resp = requests.get("https://woniuxy.com/")

html = etree.HTML(resp.text)  # 返回一个html对象
items = html.xpath("//div[@class='banner-guide']//a[1]")
print(type(items))
for item in items:
    print(item.text)
    print(item.get('href'))  # 使用get方法获取html标签的属性值
# print(resp.text)

if __name__ == "__main__":
    run_code = 0
