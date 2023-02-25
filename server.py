import socket

HOST = '192.168.50.245' #NEEDS TO BE CHANGED FOR EACH HOST
PORT = 4206

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    client_socket, address = server.accept()
    print(f"Connected to {address}")
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Message from client is : {message}")
    client_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    client_socket.close()
    print(f"Connection ended")