import socket

HOST = TODO
PORT = TODO

with socket.socket(TODO, TODO) as s:
    socket.bind((HOST, PORT))
    s.listen()
    conn, addr = socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
