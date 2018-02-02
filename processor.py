import re
import speech_recognition as sr
from assistant import Assistant

class Processor(object):
    recognizer = sr.Recognizer()

    def __init__(self, audio):
        object.__init__(self)
        self.audio = audio
        self.phrase = ""

    def run(self):
        success = self.recognize_phrase()
        if success:
            success = self.execute_command()

        return success

    def recognize_phrase(self):
        try:
            self.phrase = Processor.recognizer.recognize_google_cloud(self.audio)
            understood = True
        except:
            understood = False

        return understood

    def execute_command(self):
        matched = False
        for command in Assistant.commands():
            if re.search(command[0], self.phrase, re.I):
                matched = True
                args = re.search(command[0], self.phrase, re.I).groups()

                if len(args) > 0:
                    command[1](args)
                else:
                    command[1]()

        return matched
