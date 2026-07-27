import json
import os

class AssistantMemory:

    def __init__(self):

        self.last_app = None
        self.last_browser = None
        self.last_topic = None

        self.memory_file = "jarvis_memory.json"

        self.personal_memory = {}

        self.load_memory()

    def load_memory(self):

        if os.path.exists(self.memory_file):

            try:

                with open(self.memory_file, "r") as file:

                    self.personal_memory = json.load(file)

            except exception:

                self.personal_memory = {}

        else:

            self.personal_memory = {}    

    def save_memory(self): 

        with open(self.memory_file, "w") as file:

            json.dump(
                self.personal_memory,
                file,
                indent=4
            )  

    def remember(self, key, value):

        self.personal_memory[key] = value

        self.save_memory()      

    def recall(self, key):

        return self.personal_memory.get(key)

    def forget(self, key):

        if key in self.personal_memory:

            del self.personal_memory[key]

            self.save_memory()           