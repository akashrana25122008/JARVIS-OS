import sys
import threading

from responses import (
    random_response,
    WAKE_RESPONSES,
)
from context import JarvisContext

from speech import Speaker
from command_manager import CommandManager

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from window import JarvisWindow
from voice import VoiceRecognizer

from state import AssistantState


def run():
    app = QApplication(sys.argv)

    window = JarvisWindow()

    voice = VoiceRecognizer()

    speaker = Speaker()

    context = JarvisContext()

    context.window = window
    context.voice = voice
    context.speaker = speaker

    manager = CommandManager(context)

    current_state = AssistantState.SLEEP

    voice.recognized.connect(window.set_recognized_text)
    def process_text(text):

        nonlocal current_state

        if text == "Could not understand.":
           return

        if current_state == AssistantState.SLEEP:

           if text == "jarvis":
              current_state = AssistantState.COMMAND
              print("STATE -> COMMAND")
              window.wake_word_detected()

              speaker.speak(
                  random_response(WAKE_RESPONSES)
              )

           return

        if current_state == AssistantState.COMMAND:

            # Sleep Commands
            if text.lower() in [
                 "goodbye",
                 "good bye",
                 "bye",
                 "sleep",
                 "go to sleep",
                 "exit",
                 "stop listening"
            ]:

               speaker.speak("Going to sleep.")

               current_state = AssistantState.SLEEP

               print("STATE -> SLEEP")

               return

        voice.stop()

        window.set_action("Thinking...")

        manager.process(text)

        speaker.wait_until_done()

        window.set_action("Ready")

        voice.start()

        print("STATE -> COMMAND")
    voice.recognized.connect(process_text)  
         

    voice_thread = threading.Thread(
    target=voice.run,
    daemon=True
    )

    voice_thread.start()

    window.set_status("READY TO LISTEN")
    QTimer.singleShot(
    3000,
    lambda: window.set_status("LISTENING...")
    )


    window.show()

    speaker.speak("System online.")

    sys.exit(app.exec())