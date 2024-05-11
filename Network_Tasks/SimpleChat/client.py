#Client Side:
from socket import *

host = "127.0.0.1"
port = 1900

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((host, port))
print("Server Connection Successful")

buffer = None
while True:
    send_msg = input("Client:")
    if send_msg.lower() == 'bye':
        soc.send(send_msg.encode("utf-8"))
        break
    soc.send(send_msg.encode("utf-8"))

    recv_msg = b""
    while True:
        chunk = soc.recv(buffer or 4096)
        if not chunk:
            break
        recv_msg += chunk

    recv_msg = recv_msg.decode("utf-8")
    if recv_msg.lower() == 'bye':
        break
    print("Server:", recv_msg)

soc.close()
