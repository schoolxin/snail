# -*- coding:utf-8 -*-
# @FileName  :beautifulSoupDemo01.py
# @Time      :2023/10/4 11:24
# @Author    :dzz
# @Function  :
from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>我是title</title>
</head>
<body>
    <p class='p1'>p1</p>
    <p class='p1'>p2</p>
    <div id="div1">
        <p class='p2 p1'>
            <a href="">子孙</a>
        </p>
    </div>
    <div class="panel-body">
        <ul id="ul1">
            <li class="ele">1</li>
            <li class="ele" data='root'>2</li>
        </ul>
        <ul id="ul2">
            <li>3</li>
        </ul>
    </div>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.div.children)
# 直接子节点
for index, item in enumerate(soup.div.children):
    pass
    # print(index, item)
# 子孙节点
print("子孙节点")
for index, item in enumerate(soup.div.descendants):
    pass
    # print(index, item)
print("find_all 根据标签名进行查找")
# 根据名字查找
print(soup.find_all('p'))
# 根据属性查找
print("find_all 根据属性查找")
# print(soup.find_all(attrs={'id': 'div1'}))
# print(soup.find_all(attrs={'class': 'p1'}))
print(soup.find_all(class_='p1'))
# 根据文本进行选择
print("find_all 根据文本查找")
print(soup.find_all(string='子孙'))

print("css 选择器 select()")
print(soup.select("#div1 .p1"))
for ul in soup.select("ul"):
    print(ul.get('id'))  # 获取所有ul元素的id属性

print("属性结合标签、样式选择器使用")
print(soup.select('.panel-body li[data="root"]'))

print("获取文字内容")
for li in soup.select("li"):
    print(li.get_text())
if __name__ == "__main__":
    run_code = 0
