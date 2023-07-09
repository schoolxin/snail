import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("woniuclient".encode(), ('127.0.0.1', 9999))

print(client.recv(1024).decode())

client.close()
