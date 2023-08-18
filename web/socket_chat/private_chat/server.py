# -*- coding:utf-8 -*-
# @FileName  :server.py
# @Time      :2023/7/28 9:55
# @Author    :dzz
# @Function  :
# 1、需要在服务器端 保存用户名和链接对象的对应关系 ，方便后面通过用户名找到对应的链接对象 然后发送数据
# 2.服务器转发消息前，需要判断消息中是否有@符号 如果有需要解析出用户名，然后根据用户名找到对应的链接对象
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 TCP

server.bind(('0.0.0.0', 8000))

server.listen()  # 监听
print("服务器已经启动，欢迎来聊")

print("等待客户端链接》》》》》》》》》》》》》》》")

client_sock = {}  # 保存了所有客户端链接对象和昵称的对应关系 {sock:username}


def handle_chat(sock):
    try:
        user_name = sock.recv(1024).decode()
        client_sock[sock] = user_name
        for client in client_sock.keys():  # 群发给所有客户端 提示谁谁上线了
            client.send(("欢迎" + user_name + "加入群聊").encode())
        while True:
            data = sock.recv(1024).decode()  # 获取数据的大小 一次接收1K
            # print("接收到消息{}".format(data.decode()))
            # 服务器接收到数据后进行转发给其他客户端
            send_data = '【' + user_name + '】' + "说:" + data
            # "@王五 hhhhh"
            # ''.startswith()
            if data.startswith('@'):  # 说明当前是私聊
                msg = data.split(' ')  # 拆分出 用户名和消息体
                private_name = msg[0][1:]
                for k, v in client_sock.items():
                    if v == private_name:
                        k.send(send_data.encode())
            else:
                if client_sock:
                    for client in client_sock:
                        client.send(send_data.encode())
            print("消息转发成功！！！")
    except Exception as e:
        client_sock.pop(sock)
        for client in client_sock.keys():
            client.send("{}已经退出群聊".format(user_name).encode())


while True:
    sock, addr = server.accept()  # 阻塞方法 等待客户端的链接 sock 当前的链接对象     addr 表示链接上来的地址 可以区分不同的客户端  接受不同的客户端链接请求
    client_sock[sock] = ''
    sock.send("请输入您的昵称".encode())

    # client_sock.append(sock)
    # 每连接上来一个客户端就创建一个线程与之交互
    thread_client = threading.Thread(target=handle_chat, args=(sock,))
    thread_client.start()
