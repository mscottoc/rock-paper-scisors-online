import socket

HOST = '192.168.50.245' #NEEDS TO BE CHANGED FOR EACH HOST
PORT = 4206

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello world".encode('utf-8'))
print(socket.recv(1024))