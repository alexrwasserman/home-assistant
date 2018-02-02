import os, sys
import RPi.GPIO as GPIO
import speech_recognition as sr
from squid import *
from processor import Processor
from constants import *

sys.path.append(SNOWBOY_DECODER_LOCATION)
import snowboydecoder
sys.path.pop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_STRIP_GPIO_LEAD, GPIO.OUT)

def main():
    recognizer = sr.Recognizer()
    rgb = Squid(RED_GPIO_LEAD, GREEN_GPIO_LEAD, BLUE_GPIO_LEAD)
    snowboy_detector = snowboydecoder.HotwordDetector(
        SNOWBOY_HOTWORD_LOCATION,
        sensitivity=0.5,
        audio_gain=1
    )

    while True:
        snowboy_detector.listen()
        rgb.set_color(GREEN)

        with sr.Microphone(device_index=2) as source:
            audio = recognizer.listen(source=source)
            rgb.set_color(BLUE)

            processor = Processor(audio=audio)
            success = processor.run()

            if not success:
                Processor.rgb.set_color(RED)
                sleep(1)

            Processor.rgb.set_color(OFF)

if __name__ == '__main__':
    main()
