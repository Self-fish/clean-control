from dependency_injector import providers, containers

from controller.MotorController import MotorController


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    motor_controller = providers.Singleton(MotorController)
