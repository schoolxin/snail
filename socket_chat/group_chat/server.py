# -*- coding:utf-8 -*-
# @FileName  :server.py
# @Time      :2023/7/28 9:55
# @Author    :dzz
# @Function  :
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 TCP

server.bind(('0.0.0.0', 8000))

server.listen()  # 监听
print("服务器已经启动，欢迎来聊")

print("等待客户端链接》》》》》》》》》》》》》》》")

client_sock = []


def handle_chat(sock):
    try:
        user_name = sock.recv(1024).decode()
        for client in client_sock:
            client.send(("欢迎" + user_name + "加入群聊").encode())
        while True:
            data = sock.recv(1024).decode()  # 获取数据的大小 一次接收1K
            # print("接收到消息{}".format(data.decode()))
            # 服务器接收到数据后进行转发给其他客户端
            # send_data = data.encode()
            if client_sock:
                for client in client_sock:
                    client.send((user_name + "说:" + data).encode())
            print("消息转发成功！！！")
    except Exception as e:
        client_sock.remove(sock)
        for client in client_sock:
            client.send("{}已经退出群聊".format(user_name).encode())


while True:
    sock, addr = server.accept()  # 阻塞方法 等待客户端的链接 sock 当前的链接对象     addr 表示链接上来的地址 可以区分不同的客户端  接受不同的客户端链接请求
    sock.send("请输入您的昵称".encode())
    client_sock.append(sock)
    # 每连接上来一个客户端就创建一个线程与之交互
    thread_client = threading.Thread(target=handle_chat, args=(sock,))
    thread_client.start()
