import socket
import sys

from Container import Container


def listen_messages():
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", 2000))
    service.listen(1)
    client, address = service.accept()
    while client:
        while True:
            message = client.recv(1024)
            print(message.decode("utf-8"))
    client.close()
    service.close()


if __name__ == '__main__':

    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    listen_messages()
