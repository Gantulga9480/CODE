import socket

IP = "173.194.93.96"
PORT = 5555

address = (IP, PORT)

chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

chat_socket.bind(address)

chat_socket.listen()
print(f"Listening new connection from IP> {IP}:{PORT}")

while True:
    conn, add = chat_socket.accept()
    print(f"Accepted new connection from {add}")
