from assistant.assistant import OpenAIAssistant
from main import load_api_key_from_file
from openaiclient.client import OpenAIClient
from thread.thread import OpenAIThread

if __name__ == '__main__':
    # assistant = OpenAIAssistant(name="Camille Ghost").build()
    # thread = OpenAIThread().build()
    api_key = load_api_key_from_file()
    client = OpenAIClient(api_key=api_key)
    # client.create_with_thread(thread_id=thread.id, prompt="Salut que veux-tu savoir de moi ? ")
    # client.run(thread_id=thread.id, assistant_id=assistant.id)

    # client.get_answers(thread_id=thread.id)
    # print("Thread ID: ", thread.id)
    # print("Assistant ID: ", assistant.id)

    # client.send_message(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
    #                     prompt="Je travaille dans une association qui s'appelle VRAC (Vers un Réseau d'Achat en Commun), tu connais ? Si oui, résume moi ce que tu sais")
    client.run(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
               assistant_id="asst_BIOHIqf1VqZGuiQzapiRufg7")
    client.get_answers(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej")