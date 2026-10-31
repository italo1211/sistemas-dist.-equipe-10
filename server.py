import socket
import threading

PORT = 4444
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "SAIR"
maior_lance = 0
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
melhor_lance_pessoa = []

def atualizar():
    global maior_lance
    lance_velho = 0
    while True:
        if lance_velho != maior_lance:
            mensagem = f"Novo maior lance definido por {melhor_lance_pessoa[-1]}! Maior lance: {maior_lance}".encode(FORMAT)
            lance_velho = maior_lance
            for client in clients:
                client.send(mensagem)

def handle_client(conn, addr):
    print(f"[NOVO PARTICIPANTE!] {addr} se conectou.")
    
    def send(msg):
        message = msg.encode(FORMAT)
        
        conn.send(message)
    
    connected = True
    global maior_lance

    send(f"Bem vindo(a) ao leilão Do grupo 10! O maior lance atual é de {maior_lance}. Dê seu lance com 'BID <valor>', consulte o estado atual com 'STATUS' ou saia com 'SAIR'")
    while connected:
        
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            send(f"Conexão encerrada.")
            connected = False
        elif msg == "STATUS":
            print(f"[{addr}] {msg}")
            send(f"Estado atual do leilão: participantes: {threading.active_count() - 2}. Lance mais alto: {maior_lance}")
        elif "BID" in msg:
            print(f"[{addr}] {msg}")
            valor = int(msg.replace("BID ", ""))
            if valor > maior_lance:
                melhor_lance_pessoa.append(addr)
                maior_lance = valor
                send(f"Você deu o maior lance!")
            else:
                send(f"Esse lance não é maior que o maior lance atual de {maior_lance}.")
        else:
            send(f"Comando não reconhecido.")
    print("FIM DE CONEXÃO")
    conn.close()

thread_atualizar = threading.Thread(target=atualizar)
thread_atualizar.start()
def start():
    server.listen()
    print(f"[OUVINDO] O servidor está aguardando os participantes do leilão aqui: {SERVER}!")
    while True:
        conn, addr =  server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[PARTICIPANTES ATIVOS] {threading.active_count() - 2}")

print("[INICIANDO] O servidor está inciando...")
start()

