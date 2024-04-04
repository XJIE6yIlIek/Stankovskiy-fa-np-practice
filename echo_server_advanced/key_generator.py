from cryptography.fernet import Fernet


with open("secret_key.txt", "w") as file:
    key = Fernet.generate_key()
    file.write(key.decode())
