import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp

server.bind(('0.0.0.0', 9999))

data, addr = server.recvfrom(1024) # 获取客户端发送来的数据以及客户端的地址

print(data.decode())


server.sendto("hello".encode(),addr)

server.close()