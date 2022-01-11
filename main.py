import socket
import sys

from Container import Container
from domain.usecase.HandleCoverUseCase import HandleCoverUseCase

if __name__ == '__main__':

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    handle_cover = HandleCoverUseCase()

    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", 2000))
    service.listen(1)
    client, address = service.accept()
    while client:
        while True:
            message = bytearray(client.recv(1024))
            del message[0]
            if message.decode("UTF-8") == "COVER_UP":
                print("We move the motor")
                handle_cover.cover_up()
            print(message)
            print(bytearray("COVER_UP"))
    client.close()
    service.close()

