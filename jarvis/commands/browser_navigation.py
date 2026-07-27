import pyautogui


# --------------------------
# Action Functions
# --------------------------

def refresh_page():
    pyautogui.press("f5")

def scroll_down():
    pyautogui.scroll(-700)


def scroll_up():
    pyautogui.scroll(700)    

def go_back():
    pyautogui.hotkey("alt", "left")


def go_forward():
    pyautogui.hotkey("alt", "right")    


# --------------------------
# Command Map
# --------------------------

NAVIGATION_COMMANDS = {

    "refresh": (refresh_page, "Refreshing page."),
    "reload": (refresh_page, "Refreshing page."),

    "scroll down": (scroll_down, "Scrolling down."),
    "scroll up": (scroll_up, "Scrolling up."),

    "go back": (go_back, "Going back."),
    "back": (go_back, "Going back."),

    "go forward": (go_forward, "Going forward."),
    "forward": (go_forward, "Going forward."),
}


# --------------------------
# Execute Navigation
# --------------------------

def execute_browser_navigation(text):

    text = text.lower()

    for command, (action, response) in NAVIGATION_COMMANDS.items():

        if command in text:

            action()

            return response

    return None