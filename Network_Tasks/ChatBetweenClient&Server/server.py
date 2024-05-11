#Server Side:
from socket import *
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 3000
server.bind((host, port))
server.listen()

clients = []
clients_names = []


def brdcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)


def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            brdcast(msg, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = clients_names[index]
            brdcast('{} left!'.format(name).encode('ascii'), client)
            clients_names.remove(name)
            break


def recv():
    while True:
        client, addr = server.accept()
        print("Connected with {}".format(str(addr)))

        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        clients_names.append(name)
        clients.append(client)

        print("Nickname is {}".format(name))
        brdcast("{} joined!".format(name).encode('ascii'), client)
        client.send('Connected to Server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


recv()
