from dependency_injector.wiring import Provide, inject

from Container import Container
from controller.MotorController import MotorController


class HandleCoverUseCase:

    @inject
    def __init__(self, motor_controller: MotorController = Provide[Container.motor_controller]):
        self.__motor_controller = motor_controller

    def cover_up(self):
        self.__motor_controller.set_direction_up()
        self.__motor_controller.move_motor()

    def cover_down(self):
        self.__motor_controller.set_direction_up()
        self.__motor_controller.move_motor()
