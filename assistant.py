import os
import RPi.GPIO as GPIO
from weather import Weather
from gtts import gTTS
from constants import POWER_STRIP_GPIO_LEAD

class Assistant(object):
    def __init__(self):
        object.__init__(self)

    @classmethod
    def commands(cls):
        return [
            (r"lights on", Assistant.turn_lights_on),
            (r"lights off", Assistant.turn_lights_off),
            (r"set an alarm for (.+)", Assistant.set_alarm),
            (r"weather today", Assistant.current_weather)
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

    @classmethod
    def current_weather(cls):
        try:
            location = Weather().lookup_by_location('ann arbor')
            condition = location.condition()

            fahrenheit = int((int(condition.temp()) * 9 / 5) + 32)

            report = 'The weather today is ' + str(fahrenheit) + ' degrees'
            report += ' and ' + condition.text()
        except:
            report = 'The weather is unavailable'

        tts = gTTS(text=report, lang='en', slow=False)
        tts.save('weather.mp3')
        os.system('omxplayer weather.mp3')
        os.remove('weather.mp3')
