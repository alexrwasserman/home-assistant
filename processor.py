import speech_recognition as sr
import threading, re
from assistant import Assistant

class Processor(threading.Thread):
    recognizer = sr.Recognizer()

    commands = [
        (r"lights on", Assistant.turn_lights_on),
        (r"lights off", Assistant.turn_lights_off),
        (r"set an alarm for (.+)", Assistant.set_alarm)
    ]

    def __init__(self, audio, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.audio = audio
        self.phrase = ""

    def run(self):
        self.recognize_phrase()
        self.execute_command()

    def recognize_phrase(self):
        try:
            self.phrase = Processor.recognizer.recognize_google_cloud(self.audio)
            print(self.name + " thinks you said '" + self.phrase + "'")
        except sr.UnknownValueError:
            print(self.name + " could not understand audio")
        except sr.RequestError as e:
            print(self.name + " could not request results from Google Cloud Speech recognition service; {0}". format(e))

    def execute_command(self):
        matched = False
        for command in Processor.commands:
            if re.search(command[0], self.phrase, re.I):
                matched = True
                args = re.search(command[0], self.phrase, re.I).groups()

                if len(args) > 0:
                    command[1](Assistant, args)
                else:
                    command[1](Assistant)

        if not matched:
            print("Assistant is not familiar with that command")
