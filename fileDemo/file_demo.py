# -*- coding:utf-8 -*-
# @FileName  :file_demo.py
# @Time      :2023/7/3 17:26
# @Author    :dzz
# @Function  :

# f = open(r'file/python.txt', encoding='UTF-8')
# print(f.read(1))
# while True:
#     ch = f.read(1)
#     if not ch:
#         break
#     print(ch,end='')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     if line[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         print(line,end='')

# lines = f.readlines()
# for line in lines:
#     print(line, end="")
# f.close()
# with open(r'file\python2.txt', encoding='UTF-8') as f:
#     print(f)
#     for line in f:
#         print(line,end='')

with open(r"file\write.txt", mode='w',encoding='utf8') as f:
    # print("文件指针位置", f.tell())
    # f.seek(-3, 1)
    # print(f.read(1))
    f.write("欢迎大家来蜗牛学Python\n")
    f.writelines(['举头望明月\n','低头思故乡']) # 列表中的每一个元素就是文件中的一行 批量写入的话 就放使用writelines

import requests

r = requests.get("https://dss2.bdstatic.com/5bVYsj_p_tVS5dKfpU_Y_D3/res/r/image/2021-3-4/hao123%20logo.png")
with open('baidu.png',mode='wb') as f:
    # print(r.text)
    # print(r.content)
    f.write(r.content)


