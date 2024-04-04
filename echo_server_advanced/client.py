import socket
from IPy import IP


def start_client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    while True:
        data = sock.recv(1024)
        print(f"{host}: {data.decode()}")
        msg = input()
        if msg == "exit":
            break
        sock.send(str.encode(msg))

    sock.close()


def get_ip_port():
    while True:
        host = input("Input host ip:")
        port = input("Input host port: ")

        try:
            if IP(host) and (0 < int(port) <= 65535):
                break
        except ValueError:
            print("Invalid IP and/or port, using default IP and port (localhost:9999)")
            return "localhost", 9999

    return host, int(port)


host, port = get_ip_port()
start_client(host, port)