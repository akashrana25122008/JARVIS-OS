import asyncio
import os
import queue
import threading

import edge_tts
from playsound3 import playsound


VOICE = "en-IN-PrabhatNeural"


class Speaker:

    def __init__(self):

        self.queue = queue.Queue()

        self.thread = threading.Thread(
            target=self._worker,
            daemon=True
        )

        self.thread.start()

    def speak(self, text):

        self.queue.put(text)

    async def _generate(self, text):

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE
        )

        await communicate.save("jarvis_voice.mp3")

    def _worker(self):

        while True:

            text = self.queue.get()

            print("JARVIS :", text)

            asyncio.run(self._generate(text))

            playsound("jarvis_voice.mp3")

            try:
                os.remove("jarvis_voice.mp3")
            except:
                pass

            self.queue.task_done()

    def wait_until_done(self):
        self.queue.join()        