from dependency_injector import providers, containers

from controller.MotorController import MotorController
from controller.RelayController import RelayController

EMPTY_BOMB_PIN = 3
FILL_BOMB_PIN = 5
COVER_MOTOR_PIN = 4


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    cover_relay_controller = providers.Factory(RelayController, COVER_MOTOR_PIN)
    motor_controller = providers.Singleton(MotorController)
    water_bomb_relay_controller = providers.Factory(RelayController, FILL_BOMB_PIN)
    empty_bomb_relay_controller = providers.Factory(RelayController, EMPTY_BOMB_PIN)
