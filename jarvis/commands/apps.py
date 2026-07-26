import os


APP_COMMANDS = {

    "calculator": {
        "open": "calc",
        "process": "CalculatorApp.exe"
    },

    "notepad": {
        "open": "notepad",
        "process": "notepad.exe"
    },

    "paint": {
        "open": "mspaint",
        "process": "mspaint.exe"
    },

}

def execute_app_command(text):

    text = text.lower()

    for app, data in APP_COMMANDS.items():

        if app not in text:
            continue

        # OPEN
        if any(word in text for word in ["open", "launch", "start"]):

            os.system(f"start {data['open']}")

            return f"Opening {app.title()}."

        # CLOSE
        if any(word in text for word in ["close", "exit", "kill"]):

            os.system(f"taskkill /IM {data['process']} /F")

            return f"Closing {app.title()}."

    return None