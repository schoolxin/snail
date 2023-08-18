import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个TCP连接
server.bind(('0.0.0.0', 8888))
server.listen()  # 监听

sock, addr = server.accept()  # 接收客户端的连接 sock 本次连接创建的socket对象 addr 客户端的地址信息 是一个阻塞方法

data = sock.recv(1024)  # 接收客户端的数据
print(data.decode('utf-8'))  # 二进制的数据需要解码 编程string
sock.send("hello,client".encode('utf-8'))
server.close()
sock.close()
