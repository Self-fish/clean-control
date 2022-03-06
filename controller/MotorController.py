import time
import RPi.GPIO as GPIO
from controller.Direction import Direction

DIRECTION_PIN = 24
STEP_PIN = 26
NUMBER_OF_STEPS = 3000
MICRO_PAUSE = 0.0005


class MotorController:

    def __init__(self):
        self.__direction_pin = DIRECTION_PIN
        self.__step_pin = STEP_PIN
        self.__steps = NUMBER_OF_STEPS
        self.__micro_pause = MICRO_PAUSE
        self.__direction = Direction.UP.value
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
        GPIO.setup(self.__step_pin, GPIO.OUT)

    def set_direction_up(self):
        self.__direction = Direction.UP.value

    def set_direction_down(self):
        self.__direction = Direction.DOWN.value

    def move_motor(self):
        GPIO.output(self.__direction_pin, self.__direction)
        for x in range(0, self.__steps):
            GPIO.output(self.__step_pin, True)
            time.sleep(self.__micro_pause)
            GPIO.output(self.__step_pin, False)
            time.sleep(self.__micro_pause)
