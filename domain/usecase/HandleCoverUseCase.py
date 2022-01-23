from dependency_injector.wiring import Provide, inject

from Container import Container
from controller.MotorController import MotorController
from controller.RelayController import RelayController
from controller.RelayStatus import RelayStatus


class HandleCoverUseCase:

    @inject
    def __init__(self, motor_controller: MotorController = Provide[Container.motor_controller],
                 relay_controller: RelayController = Provide[Container.relay_controller]):
        self.__motor_controller = motor_controller
        self.__relay_controller = relay_controller

    def cover_up(self):
        self.__start_motor()
        self.__motor_controller.set_direction_up()
        self.__motor_controller.move_motor()
        self.__stop_motor()

    def cover_down(self):
        self.__start_motor()
        self.__motor_controller.set_direction_down()
        self.__motor_controller.move_motor()
        self.__stop_motor()

    def __start_motor(self):
        self.__relay_controller.update_relay_status(RelayStatus.ON)

    def __stop_motor(self):
        self.__relay_controller.update_relay_status(RelayStatus.OFF)
