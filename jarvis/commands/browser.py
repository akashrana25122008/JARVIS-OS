import webbrowser
from urllib.parse import quote_plus

SEARCH_ENGINES = {

    "google": "https://www.google.com/search?q={}",

    "youtube": "https://www.youtube.com/results?search_query={}",

    "github": "https://github.com/search?q={}",

}


BROWSER_COMMANDS = {

    "youtube": "https://youtube.com",

    "google": "https://google.com",

    "github": "https://github.com",

    "gmail": "https://mail.google.com",

    "chatgpt": "https://chat.openai.com",

}


def execute_browser_command(text):

    text = text.lower()

    # ------------------------
    # Google Search
    # ------------------------

    if text.startswith("search "):

        query = text.replace("search ", "", 1)

        engine = "google"

        for site in SEARCH_ENGINES:

            if f"on {site}" in query or f"in {site}" in query:

                engine = site
                query = (
                    query.replace(f"on {site}", "")
                    .replace(f"in {site}", "")
                    .strip()
                )
                break

        url = SEARCH_ENGINES[engine].format(
        quote_plus(query)
        )    

        webbrowser.open(url)

        return f"Searching {engine.title()} for {query}."
    # ------------------------
    # Website Commands
    # ------------------------

    for site, url in BROWSER_COMMANDS.items():

        if site not in text:
            continue

        if any(word in text for word in ["open", "launch", "start"]):

            webbrowser.open(url)

            return f"Opening {site.title()}."

    return None