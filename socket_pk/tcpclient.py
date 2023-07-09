import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个TCP连接

client.connect(('127.0.0.1', 8888))


client.send('woniu'.encode(encoding='utf-8'))

data = client.recv(1024)
print(data.decode())

client.close()