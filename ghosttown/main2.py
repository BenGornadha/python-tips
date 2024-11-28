from fastapi import APIRouter

from assistant.assistant import OpenAIAssistant
from main import load_api_key_from_file
from openaiclient.client import OpenAIClient
from thread.thread import OpenAIThread


send_prompt_router = APIRouter(
    prefix="/ghost",
    tags=["send"]
)


def http_collect_bu_entities_for_all_surveys(bu: str, entity: Entity) -> fastapi.Response:
    jr = collect(bu=bu.upper(), entity=entity)
    return create_appropriate_http_response(jr)


@send_prompt_router.post("/bu/{bu}/{entity}")
def send_prompt(prompt: str):
    client.send_message(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
                        prompt=prompt)
    client.run(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
               assistant_id="asst_BIOHIqf1VqZGuiQzapiRufg7")


def read_conversation():
    messages = client.get_answers(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej")
    return messages

if __name__ == '__main__':
    api_key = load_api_key_from_file()
    client = OpenAIClient(api_key=api_key)

    send_prompt(prompt="Salut comment ça va ? ")
    read_conversation()

    # client.send_message(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
    #                     prompt="Je travaille dans une association qui s'appelle VRAC (Vers un Réseau d'Achat en Commun), tu connais ? Si oui, résume moi ce que tu sais")
    # client.run(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej",
    #            assistant_id="asst_BIOHIqf1VqZGuiQzapiRufg7")
    # client.get_answers(thread_id="thread_es8J9GI8tyzagdy4RkMXqBej")



    # assistant = OpenAIAssistant(name="Camille Ghost").build()
    # thread = OpenAIThread().build()
    # client.create_with_thread(thread_id=thread.id, prompt="Salut que veux-tu savoir de moi ? ")
    # client.run(thread_id=thread.id, assistant_id=assistant.id)

    # client.get_answers(thread_id=thread.id)
    # print("Thread ID: ", thread.id)
    # print("Assistant ID: ", assistant.id)
