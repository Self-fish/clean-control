from dependency_injector import providers, containers

from controller.MotorController import MotorController
from controller.RelayController import RelayController


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    cover_relay_controller = providers.Factory(RelayController, 4)
    motor_controller = providers.Singleton(MotorController)
    water_bomb_relay_controller = providers.Factory(RelayController, 5)
    empty_bomb_relay_controller = providers.Factory(RelayController, 3)
