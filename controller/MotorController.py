import time
import RPi.GPIO as GPIO
from controller.Direction import Direction


class MotorController:

    def __init__(self):
        self.__direction_pin = 24
        self.__step_pin = 26
        self.__steps = 3000
        self.__micro_pause = 0.0005
        self.__direction = Direction.UP
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
        GPIO.setup(self.__step_pin, GPIO.OUT)

    def set_direction_up(self):
        self.__direction = Direction.UP

    def set_direction_down(self):
        self.__direction = Direction.DOWN

    def move_motor(self):
        GPIO.output(self.__direction_pin, self.__direction)
        for x in range(0, self.__steps):
            GPIO.output(self.__step_pin, True)
            time.sleep(self.__micro_pause)
            GPIO.output(self.__step_pin, False)
            time.sleep(self.__micro_pause)
