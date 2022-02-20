from dependency_injector.wiring import Provide, inject

from Container import Container
from controller.RelayController import RelayController
from controller.RelayStatus import RelayStatus


class HandleEmptyBombUseCase:

    def __init__(self, bomb_relay_controller: RelayController = Provide[Container.empty_bomb_relay_controller]):
        self.__bomb_relay_controller = bomb_relay_controller
        self.__bomb_relay_controller.update_relay_status(RelayStatus.OFF)

    def empty_aquarium(self):
        self.__bomb_relay_controller.update_relay_status(RelayStatus.ON)

    def stop_empty_aquarium(self):
        self.__bomb_relay_controller.update_relay_status(RelayStatus.OFF)