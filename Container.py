from dependency_injector import providers, containers

from controller.MotorController import MotorController
from controller.RelayController import RelayController


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    relay_controller = providers.Factory(RelayController, 4)
    motor_controller = providers.Singleton(MotorController)
