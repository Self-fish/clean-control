import socket
import sys

from Container import Container
from domain.usecase.HandleCoverUseCase import HandleCoverUseCase
from domain.usecase.HandleFillingBombUseCase import HandleFillingBombUseCase

if __name__ == '__main__':

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    handle_cover = HandleCoverUseCase()
    handle_water_bomb = HandleFillingBombUseCase()

    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", 2000))
    service.listen(1)

    while True:
        client, address = service.accept()
        try:
            while True:
                message = client.recv(1024)
                if message:
                    if message.decode("UTF-8") == "COVER_UP":
                        print("COVER_UP")
                        handle_cover.cover_up()
                    elif message.decode("UTF-8") == "COVER_DOWN":
                        print("COVER_DOWN")
                        handle_cover.cover_down()
                    elif message.decode("UTF-8") == "FILLING_BOMB_ON":
                        print("FILLING_BOMB_ON")
                        handle_water_bomb.fill_aquarium()
                    elif message.decode("UTF-8") == "FILLING_BOMB_OFF":
                        print("FILLING_BOMB_OFF")
                        handle_water_bomb.stop_filling_aquarium()
                else:
                    break
        finally:
            client.close()

