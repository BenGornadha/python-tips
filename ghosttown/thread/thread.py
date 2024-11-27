from openai import OpenAI

from main import load_api_key_from_file


class OpenAIThread:

    def __init__(self):
        self.current_thread = None
        self._thread_id = None

    def build(self):
        self.current_thread = OpenAI(api_key=load_api_key_from_file()).beta.threads.create()
        self._thread_id = self.current_thread.id
        return self.current_thread

