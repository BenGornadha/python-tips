from openai import OpenAI

from main import load_api_key_from_file


class OpenAIAssistant:

    def __init__(self, name: str):
        self._name = name

    def build(self):
        return OpenAI(api_key=load_api_key_from_file()).beta.assistants.create(
            name=self._name,
            instructions="T'es français. "
                         "Tu peux questionner une personne sur son travail,"
                         " jusqu'à que tu comprennnes ce qu'elle fait dans tous ses détails."
                         " L'objectif étant qu'un jour, quelqu'un d'autre puisse te poser des questions sur ce que faisait la personne, "
                         " et que tu sois capable d'expliquer ce qui était fait avant. Tu sers à faciliter les transmissions entre un employé qui quitte une entreprise, et celui qui remplace cet employé.",
            tools=[{"type": "file_search"}],
            model="gpt-4o-mini")
