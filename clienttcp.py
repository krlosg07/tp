import socket

HOST = TODO
PORT = TODO

with socket.socket(TODO, TODO) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
