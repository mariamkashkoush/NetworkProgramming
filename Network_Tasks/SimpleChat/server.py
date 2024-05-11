#Server Side:
from socket import *

try:
    host = "127.0.0.1"
    port = 1900

    socket = socket(AF_INET, SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(5)
    print("Server is listening on {}:{}".format(host, port))

    client_soc, client_ad = socket.accept()
    print("Connection to: ", client_ad[0])

    buffer = None
    while True:
        recv_msg = client_soc.recv(buffer or 4096).decode("utf-8")
        if not recv_msg:
            break

        if recv_msg.lower() == 'bye':
            break

        print(f"Client: {recv_msg}")

        send_msg = input("Server: ")
        if send_msg.lower() == 'bye':
            client_soc.send(send_msg.encode("utf-8"))
            break

        client_soc.send(send_msg.encode("utf-8"))

    socket.close()

except error:
    print(error)
except KeyboardInterrupt:
    print("\n\nServer is stopped by User")