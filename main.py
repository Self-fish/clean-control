import socket
import sys

from Container import Container
from domain.usecase.HandleCoverUseCase import HandleCoverUseCase
from domain.usecase.HandleEmptyBombUseCase import HandleEmptyBombUseCase
from domain.usecase.HandleFillingBombUseCase import HandleFillingBombUseCase

CLEAN_SOCKET_PORT = 2000
COVER_UP_STEP = "COVER_UP"
COVER_DOWN_STEP = "COVER_DOWN"
FILLING_BOMB_ON_STEP = "FILLING_BOMB_ON"
FILLING_BOMB_OFF_STEP = "FILLING_BOMB_OFF"
EMPTY_BOMB_ON_STEP = "EMPTY_BOMB_ON"
EMPTY_BOMB_OFF_STEP = "EMPTY_BOMB_OFF"

if __name__ == '__main__':

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    handle_cover = HandleCoverUseCase()
    handle_water_bomb = HandleFillingBombUseCase()
    empty_aquarium_bomb = HandleEmptyBombUseCase()

    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", CLEAN_SOCKET_PORT))
    service.listen(1)

    while True:
        client, address = service.accept()
        try:
            while True:
                message = client.recv(1024)
                if message:
                    if message.decode("UTF-8") == COVER_UP_STEP:
                        handle_cover.cover_up()
                    elif message.decode("UTF-8") == COVER_DOWN_STEP:
                        handle_cover.cover_down()
                    elif message.decode("UTF-8") == FILLING_BOMB_ON_STEP:
                        handle_water_bomb.fill_aquarium()
                    elif message.decode("UTF-8") == FILLING_BOMB_OFF_STEP:
                        handle_water_bomb.stop_filling_aquarium()
                    elif message.decode("UTF-8") == EMPTY_BOMB_ON_STEP:
                        empty_aquarium_bomb.empty_aquarium()
                    elif message.decode("UTF-8") == EMPTY_BOMB_OFF_STEP:
                        empty_aquarium_bomb.stop_empty_aquarium()
                else:
                    break
        finally:
            client.close()
