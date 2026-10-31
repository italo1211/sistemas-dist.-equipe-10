import socket
import threading

PORT = 4444
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive_msg():
    while True:
        message = client.recv(1024).decode(FORMAT)
        print("\n" + message)

def send_msg():
    while True:
        message = input()
        client.send(message.encode(FORMAT))

thread_receba = threading.Thread(target=receive_msg)
thread_envio = threading.Thread(target=send_msg)
thread_envio.start()
thread_receba.start()