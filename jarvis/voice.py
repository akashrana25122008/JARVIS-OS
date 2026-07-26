import time
import speech_recognition as sr

from PySide6.QtCore import QObject, Signal


class VoiceRecognizer(QObject):
    recognized = Signal(str)

    def __init__(self):
        super().__init__()

        self.recognizer = sr.Recognizer()

        self.running = True
        self.paused = False


    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print("You said:", text)

            text = text.lower()

            self.recognized.emit(text)

            return text

        except sr.UnknownValueError:

            print("Could not understand.")

            self.recognized.emit("Could not understand.")

            return ""

        except sr.RequestError:

            print("Internet error.")

            return ""

    def run(self):

        while self.running:

            if self.paused:
                time.sleep(0.05)
                continue

            self.listen()


    def stop(self):

        self.paused = True


    def start(self):

        self.paused = False        