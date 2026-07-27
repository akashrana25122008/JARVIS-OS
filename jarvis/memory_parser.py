import re


class MemoryParser:

    @staticmethod
    def parse_remember(text):

        text = text.lower().strip()

        pattern = r"remember my (.+?) is (.+)"

        match = re.match(pattern, text)

        if not match:
            return None

        key = match.group(1).strip()

        value = match.group(2).strip()

        return key, value

    @staticmethod
    def parse_recall(text):

        text = text.lower().strip()

        pattern = r"what is my (.+)"

        match = re.match(pattern, text)

        if not match:
            return None

        return match.group(1).strip()