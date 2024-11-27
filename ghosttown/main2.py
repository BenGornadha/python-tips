from assistant.assistant import OpenAIAssistant
from main import load_api_key_from_file
from openaiclient.client import OpenAIClient
from thread.thread import OpenAIThread

if __name__ == '__main__':
    assistant = OpenAIAssistant(name="Camille Ghost").build()
    thread = OpenAIThread().build()
    api_key = load_api_key_from_file()
    client = OpenAIClient(api_key=api_key)
    client.with_thread(thread_id=thread.id, prompt="Salut que veux-tu savoir de moi ? ")
    client.run(thread_id=thread.id, assistant_id=assistant.id)

    client.get_answers(thread_id=thread.id)
