import RPi.GPIO as GPIO
from constants import POWER_STRIP_GPIO_LEAD

class Assistant(object):
    def __init__(self):
        object.__init__(self)

    @classmethod
    def commands(cls):
        return [
            (r"lights on", Assistant.turn_lights_on),
            (r"lights off", Assistant.turn_lights_off),
            (r"set an alarm for (.+)", Assistant.set_alarm)
        ]

    @classmethod
    def turn_lights_on(cls):
        GPIO.output(POWER_STRIP_GPIO_LEAD, GPIO.HIGH)

    @classmethod
    def turn_lights_off(cls):
        GPIO.output(POWER_STRIP_GPIO_LEAD, GPIO.LOW)

    @classmethod
    def set_alarm(cls, args):
        print("Assistant set an alarm for " + args[0])
