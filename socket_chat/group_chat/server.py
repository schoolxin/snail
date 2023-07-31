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
    while True:
        data = sock.recv(1024)  # 获取数据的大小 一次接收1K
        # 服务器接收到数据后进行转发给其他客户端
        # send_data = data.encode()
        if client_sock:
            for client in client_sock:
                client.send(data)
        print("消息转发成功！！！")
        # print(data.decode('utf8'))  # 通过socket接收到数据是bytes类型，只有在解码之后才能正确显示
        # re_data = input("输入:")
        # sock.send(re_data.encode())


while True:
    sock, addr = server.accept()  # 阻塞方法 等待客户端的链接 sock 当前的链接对象     addr 表示链接上来的地址 可以区分不同的客户端  接受不同的客户端链接请求
    client_sock.append(sock)
    # 每连接上来一个客户端就创建一个线程与之交互
    thread_client = threading.Thread(target=handle_chat, args=(sock,))
    thread_client.start()
