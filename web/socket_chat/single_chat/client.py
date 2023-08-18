# -*- coding:utf-8 -*-
# @FileName  :client.py
# @Time      :2023/7/28 9:55
# @Author    :dzz
# @Function  :

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 TCP


client.connect(('127.0.0.1',8000))

client.send('woniu'.encode('utf8'))


data = client.recv(1024)

print(data.decode('utf8'))

client.close()
