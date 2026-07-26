import webbrowser

from commands.apps import execute_app_command
from commands.browser import execute_browser_command

from ai import ask_ai
from responses import (
    random_response,
    YOUTUBE_RESPONSES,
    UNKNOWN_RESPONSES,
    DONE_RESPONSES,
    THINKING_RESPONSES,
)


class CommandManager:

    def __init__(self, context):
        self.context = context
        self.speaker = context.speaker

    def respond(self, message):

        self.context.window.set_action(message)

        self.speaker.speak(message)

        self.context.window.set_action("Ready")    

    def process(self, text):

        print(f"Processing Command : {text}")

        text = text.lower()

        # Resolve "it" using memory

        if "it" in text:

            if self.context.memory.last_app:

               text = text.replace(
                   "it",
                   self.context.memory.last_app
               )

        elif self.context.memory.last_browser:

            text = text.replace(
                "it",
                self.context.memory.last_browser
            )

        # Check App Commands

        response = execute_app_command(text)

        if response:

            # Remember opened app
            if "opening" in response.lower():

                for app in [
                    "calculator",
                    "notepad",
                    "paint"
                ]:

                    if app in text:

                        self.context.memory.last_app = app
                        self.context.memory.last_browser = None
                        break

            self.respond(response)

            return

        # Check Browser Commands
        response = execute_browser_command(text)

        if response:

            if "opening" in response.lower():

               for site in [
                   "youtube",
                   "google",
                   "github",
                   "gmail",
                   "chatgpt"
               ]:

                   if site in text:

                       self.context.memory.last_browser = site
                       self.context.memory.last_app = None
                       break

            self.respond(response)

            return

        text = text.lower()

        # -------------------------
        # Local Commands
        # ------------------------

        # -------------------------
        # AI Fallback
        # -------------------------

        thinking = random_response(THINKING_RESPONSES)

        self.context.window.set_action(thinking)

        self.speaker.speak(thinking)

        answer = ask_ai(text)

        print(answer)

        self.respond(answer)