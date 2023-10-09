
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
'''
常见反爬手段之JS加密
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
resp = requests.get("http://www.pbc.gov.cn/rmyh/105208/index.html")
#
# # print(resp.text)
# result = re.search('<script type="text/javascript">(.*?)</script>', resp.text, re.S)
# js = result.group(1)
# js_text = js.strip().replace('\r\n', '')
# # print(js_text)
#
# res = jsbeautifier.beautify(js_text)
# # print(res)
# js2py.eval_js()
base_url = "http://www.pbc.gov.cn/"
sess = requests.Session()
driver = webdriver.Chrome()
driver.get("http://www.pbc.gov.cn/rmyh/105208/8532/index1.html")
cookies = driver.get_cookies()
print(cookies)
driver.close()

for cookie in cookies:
    sess.cookies.set(cookie['name'], cookie['value'])
resp = sess.get("http://www.pbc.gov.cn/rmyh/105208/8532/index1.html",headers=headers)
html = resp.content.decode('utf-8')

soup = BeautifulSoup(html,'lxml')
for title in soup.select(".newslist_style"):
    print(title.text,urljoin(base_url,title.select_one('a').get('href')))
#
# print(driver.find_element('class','newslist_style').text)