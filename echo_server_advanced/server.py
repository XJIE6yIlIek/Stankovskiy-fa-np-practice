import os
import socket
from datetime import datetime
from random import randint
from cryptography.fernet import Fernet


def start_server(port):
    sock = socket.socket()
    sock.bind(("", port))
    sock.listen(1)
    log_info(f"Listening on port {port}...\n")
    while True:
        conn, addr = sock.accept()
        log_info(f"Connection from {addr[0]}:{addr[1]}\n")
        login_user(addr[0], conn)
        handle_client(conn, addr[0])


def get_port():
    while True:
        port = input("Input port to be listened: ")

        try:
            if not (0 < int(port) <= 65535):
                raise ValueError
            return int(port)
        except ValueError:
            log_info("Invalid port, using default (9999)\n")
            return 9999


def handle_client(client_socket, ip):
    try:
        while True:
            rec_data = client_socket.recv(1024)
            if not rec_data:
                log_info("Client disconnected\n")
                break
            log_info(f"Received data: {rec_data.decode()}\n")
            print(f"{ip}: {rec_data.decode()}\n")
            send_data = input("Input your message: ")
            log_info(f"Sent data: {send_data}\n")
            client_socket.send(str.encode(send_data))
    except ConnectionResetError:
        log_info("Client disconnected\n")


def check_port_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("localhost", port)) == 0


def log_info(msg=""):
    with open("log.txt", "a") as file:
        file.write(f"{datetime.now()}: {msg}")
    file.close()


def login_user(ip, client_socket):
    res = ""
    with open("users.txt", "r") as file:
        for line in file:
            if ip in line:
                res = check_password(line, client_socket)

    if res == "NO":
        client_socket.send(str.encode("You've used all your attempts, connection closed"))
        client_socket.close()
        return
    elif res == "YES":
        return

    register_new_user(client_socket, ip)


def check_password(line, client_socket):
    attempts = 3
    client_socket.send(str.encode("Please, enter your password to access the server: "))
    for i in range(attempts):
        rec_pswrd = client_socket.recv(1024)
        enc_pswrd = line.split(";")[2]
        true_pswrd = password_decoder(enc_pswrd)
        if true_pswrd == rec_pswrd:
            client_socket.send(str.encode(f"Hello, {line.split(";")[1]}! You've being granted access to this server\nYou can chat now"))
            log_info(f"I've greeted and authed user {line.split(";")[1]}")
            return "YES"
        else:
            attempts -= 1
            client_socket.send(str.encode(f"This password is not correct. You have {attempts} more attempts"))

    return "NO"


def password_encoder(password):
    with open("secret_key.txt", "r") as file:
        key = str.encode(file.readline())
    cipher = Fernet(b"pI8ZFYJOOS2DcoXYMQGJTGktztZRQXA4Mbz342K-5jI=")
    encrypted_pswrd = cipher.encrypt(password)

    return encrypted_pswrd


def password_decoder(password):
    size = os.path.getsize("secret_key.txt")
    with open("secret_key.txt", "r") as file:
        key = str.encode(file.read(size))
    cipher = Fernet(b"pI8ZFYJOOS2DcoXYMQGJTGktztZRQXA4Mbz342K-5jI=")
    decrypted_pswrd = cipher.decrypt(password)

    return decrypted_pswrd


def register_new_user(client_socket, ip):
    client_socket.send(b"Input your name: ")
    name = client_socket.recv(1024)
    client_socket.send(b"You're here for the first time. Please, enter a password to login in the future: ")
    while True:
        pswrd = client_socket.recv(1024)
        if len(pswrd.decode()) < 4:
            client_socket.send(b"Your password is too short, it should be longer than 4 symbols and shorter than 20: ")
        elif len(pswrd.decode()) > 20:
            client_socket.send(b"Your password is too long, it should be longer than 4 symbols and shorter than 20: ")
        else:
            break

    enc_pswrd = password_encoder(pswrd).decode()

    with open("users.txt", "a") as file:
        file.write(f"{ip};{name.decode()};{enc_pswrd}")
    client_socket.send(str.encode(f"Hello, {name.decode()}!\nYou can chat now"))
    log_info(f"I've greeted a new user {name.decode()} and saved his password")


log_info("\n")
port = get_port()
if check_port_use(port):
    port = randint(0, 65535)
    print(f"Port is already being used, changing to another port: {port}")
start_server(port)
log_info("\n")
