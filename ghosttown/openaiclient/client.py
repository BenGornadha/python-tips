from typing import List

from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key
        self.model = model
        self._client = OpenAI(api_key=api_key)

    def create_with_thread(self, thread_id: str, prompt: str):
        self.thread = self._client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=prompt
        )

    def run(self, thread_id: str, assistant_id: str):
        self._client.beta.threads.runs.create(thread_id=thread_id,
                                              assistant_id=assistant_id)

    def get_answers(self, thread_id: str) -> List[str]:
        messages = self._client.beta.threads.messages.list(thread_id=thread_id)
        res = []
        for message in reversed(messages.data):
            print(message.role + ": " + message.content[0].text.value)
            res.append(message.role + ": " + message.content[0].text.value)
        return res

    def send_message(self, thread_id: str, prompt: str) -> None:
        try:
            message_data = {
                "thread_id": thread_id,
                "role": "user",
                "content": prompt
            }

            # Envoi du message via l'API
            self._client.beta.threads.messages.create(**message_data)
            self.run(thread_id=thread_id,
                     assistant_id="asst_BIOHIqf1VqZGuiQzapiRufg7")
        except Exception as e:
            print(e)
