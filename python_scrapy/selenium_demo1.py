import time

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

sess = requests.Session()
driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.find_element("id", 'login_field').send_keys('707643733@qq.com')
driver.find_element("id", 'password').send_keys('13571022547d')
driver.find_element('name', 'commit').click()
cookies = driver.get_cookies()
# print(cookies)
driver.close()

for cookie in cookies:
    sess.cookies.set(cookie['name'], cookie['value'])

resp = sess.get("https://github.com/schoolxin")
# print(resp.text)

soup = BeautifulSoup(resp.text,'lxml')
print(soup.select_one('.js-profile-editable-edit-button').text)

# time.sleep(10)
