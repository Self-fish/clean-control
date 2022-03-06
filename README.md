# Clean Control
The purpose of this code is to be able to handle the remote clean actions processed by the [action-api](https://github.com/Self-fish/actions-api-py) by exposing a socket service listening on the port 2000

```python
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
```

Let's review the different actions that this code is able to handle

## Cover Movements
The Cover of the aquarium is able to go up and down for cleaning purpose in order to be able to operate inside of the aquarium with ease without losing lighting. For doing that we expose a MotroController and set the direction accordly: 

```python
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
```

## Empty Aquarium
This action allows to empty the aquarium by turning ON and OFF a bomb inside by using a RelayController using the GPIO pin 3

```python
class RelayController:

    def __init__(self, pin):
        self.__io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.__pin = pin
        self.__io.pinMode(self.__pin, self.__io.OUTPUT)
        self.__io.digitalWrite(self.__pin, self.__io.HIGH)

    def update_relay_status(self, relay_status: RelayStatus):
        if relay_status == RelayStatus.ON:
            self.__io.digitalWrite(self.__pin, self.__io.LOW)
        else:
            self.__io.digitalWrite(self.__pin, self.__io.HIGH)

    def get_current_relay_status(self):
        return self.__io.digitalRead(self.__pin)
```

## Fill Aquarium
This action allows to fill the aquarium by turning ON and OFF a bomb outside by using the previous RelayController using the GPIO pin 5
