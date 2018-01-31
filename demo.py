import speech_recognition as sr
import os, sys

snowboy_location = os.path.join(os.getcwd(), "snowboy", "examples", "Python3")

sys.path.append(snowboy_location)
import snowboydecoder
sys.path.pop()

snowboy_detector = snowboydecoder.HotwordDetector(
    os.path.join("snowboy", "resources", "snowboy.umdl"),
    sensitivity=0.5,
    audio_gain=1
)

def main():
    print("Say something!")
    snowboy_detector.listen()

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = r.listen(source=source)
        print("Phrase was heard")

    # recognize speech using Google Speech Recognition
    try:
        print("Google Cloud Speech recognition thinks you said '" + r.recognize_google_cloud(audio) + "'")
    except sr.UnknownValueError:
        print("Google Cloud Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech recognition service; {0}". format(e))

if __name__ == '__main__':
    main()
