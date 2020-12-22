import socket
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 5555))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)
    msg = byte(f"{len(msg):<{HEADERSIZE}}") + msg
    client_socket.send(msg)
