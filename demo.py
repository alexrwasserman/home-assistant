import os, sys, re
from time import sleep
import RPi.GPIO as GPIO
import speech_recognition as sr
from squid import *

snowboy_location = os.path.join(os.getcwd(), "snowboy", "examples", "Python3")

sys.path.append(snowboy_location)
import snowboydecoder
sys.path.pop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def main():
    rgb = Squid(18, 23, 24)
    
    snowboy_detector = snowboydecoder.HotwordDetector(
        os.path.join("snowboy", "resources", "snowboy.umdl"),
        sensitivity=0.5,
        audio_gain=1
    )
    
    print("Say something!")
    snowboy_detector.listen()
    rgb.set_color(GREEN)

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = r.listen(source=source)
        print("Phrase was heard")
        rgb.set_color(BLUE)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google_cloud(audio)
        print("Google Cloud Speech recognition thinks you said '" + text + "'")
        rgb.set_color(OFF)

        if re.search('lights on', text):
            GPIO.output(25, GPIO.HIGH)
            sleep(5)
            GPIO.output(25, GPIO.LOW)
    except sr.UnknownValueError:
        print("Google Cloud Speech recognition could not understand audio")
        rgb.set_color(RED)
        sleep(1)
        rgb.set_color(OFF)
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech recognition service; {0}". format(e))
        rgb.set_color(RED)
        sleep(1)
        rgb.set_color(OFF)

if __name__ == '__main__':
    main()
