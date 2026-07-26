import random

# Wake responses
WAKE_RESPONSES = [
    "Yes, Rana?",
    "I'm listening.",
    "Go ahead.",
    "How can I help?",
    "Ready for your command."
]
 #thinking responses
THINKING_RESPONSES = [
    "One second...",
    "Thinking...",
    "Interesting question.",
    "Let me check.",
    "Give me a moment.",
    "I'm looking into that.",
    "Here's what I found.",
    "Let me think for a second.",
    "Checking that for you."
]

# YouTube responses
YOUTUBE_RESPONSES = [
    "Opening YouTube.",
    "Launching YouTube.",
    "Opening YouTube now.",
    "Sure. Opening YouTube."
]

# Unknown command responses
UNKNOWN_RESPONSES = [
    "Sorry, I don't know that command yet.",
    "I couldn't understand that request.",
    "That command isn't available yet.",
    "I'm still learning that command."
]

# Completion responses
DONE_RESPONSES = [
    "Done.",
    "Completed.",
    "Task finished.",
    "Anything else?"
]


def random_response(response_list):
    return random.choice(response_list)