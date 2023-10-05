# -*- coding:utf-8 -*-
# @FileName  :regex_demo01.py
# @Time      :2023/10/4 18:01
# @Author    :dzz
# @Function  :
import re

# re.search() 查找第一个匹配成功的子字符串，并且支持使用group分组，通过分组我们可以获取到目标的提取内容
content = "now: 2023-10-23 12:23:23 id: S0001 status:  nok"
# 提取上面字符串中的日期  id值 和状态
result = re.search("now:\s+\d{4}-\d{2}-\d{2}.*id:\s+S\d{4}\s+status:\s+\w+", content)
print(result)

result1 = re.search("now:\s+(\d{4}-\d{2}-\d{2}).*id:\s+(S\d+)\s+status:\s+(\w+)", content)
print(result1.groups())

# 贪婪模式和非贪婪模式
content1 = "STUID 123344 CLASSA MATHS"
result2 = re.search('STU.*(\d+)',content1) # STU.* 尽可能多的匹配 让后面的表达式尽可能少的匹配 STU.*?  非贪婪模式
# print(result2.group(1))

# re.findall 返回所有匹配到的子字符串
content2 = '''
pages:4,data:[{"BONDCODE":"12346","SNAME":"华源证券","STARTDATE":"2023-01-01T00:01:01"},{"BONDCODE":"12345","SNAME":"西部证券ST","STARTDATE":"2023-01-02T00:01:01"}]
'''

result3 = re.findall('"BONDCODE":"(\d+)"',content2)
# result4 = re.findall('"SNAME":"([\u4E00-\u9FA5A-Za-z0-9_]+)"',content2)
result4 = re.findall('"STARTDATE":"(.*?)"',content2)
print(result4)

if __name__ == "__main__":
    run_code = 0
