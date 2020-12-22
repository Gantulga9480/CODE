import socket

IP = "192.168.88.3"
PORT = 5555

address = (IP, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(address)

print("connected")