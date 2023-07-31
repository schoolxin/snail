# -*- coding:utf-8 -*-
# @FileName  :client.py
# @Time      :2023/7/28 9:55
# @Author    :dzz
# @Function  :

import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 TCP

client.connect(('127.0.0.1', 8000))


# 接收消息
def receive(client):
    while True:
        data = client.recv(1024)
        print(data.decode('utf8'))


# 发送消息
def send(client):
    while True:
        to_data = input("客户端输入:")
        client.send(to_data.encode('utf8'))  # 想服务器发送消息


threading.Thread(target=receive, args=(client,)).start()
threading.Thread(target=send, args=(client,)).start()
