import RPi.GPIO as GPIO
from main import POWER_STRIP_GPIO_LEAD

class Assistant(object):
    def __init__(self):
        object.__init__(self)

    def commands(cls):
        return [
            (r"lights on", turn_lights_on),
            (r"lights off", turn_lights_off),
            (r"set an alarm for (.+)", set_alarm)
        ]

    def turn_lights_on(cls):
        GPIO.output(POWER_STRIP_GPIO_LEAD, GPIO.HIGH)

    def turn_lights_off(cls):
        GPIO.output(POWER_STRIP_GPIO_LEAD, GPIO.LOW)

    def set_alarm(cls, args):
        print("Assistant set an alarm for " + args[0])
