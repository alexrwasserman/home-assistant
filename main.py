import speech_recognition as sr
import os, sys
from processor import Processor

recognizer = sr.Recognizer()

snowboy_location = os.path.join(os.getcwd(), "snowboy", "examples", "Python3")
snowboy_model = [os.path.join(os.getcwd(), "snowboy", "resources", "snowboy.umdl")]
snowboy_config = (snowboy_location, snowboy_model)

def main():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source)

        # continuously listen for phrases and process them
        while True:
            print("Listening for phrase")
            audio = recognizer.listen(source=source, snowboy_configuration=snowboy_config)

            processor = Processor(audio=audio)
            processor.start()

            print("Phrase heard")

if __name__ == '__main__':
    main()
