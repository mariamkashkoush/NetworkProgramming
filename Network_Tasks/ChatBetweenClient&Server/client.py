#Client Side:
from socket import *
import threading

name = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 3000
client.connect((host, port))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(name.encode('ascii'))
            else:
                print(msg)
        except:
            print("Error Occurred!!!!!!")
            client.close()
            break


def Send():
    while True:
        msg = input('')
        if msg.lower() == 'exit':
            break
        msg = '{}: {}'.format(name, msg)
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=Send)
write_thread.start()
