import openai
from typing import Dict, Any

class OpenAIClient:
    """
    Encapsule la logique d'interaction avec l'API OpenAI.
    """
    def __init__(self, api_key: str, model: str = "gpt-4-turbo") -> None:
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def send_prompt(self, prompt: str, temperature: float = 0.7) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"Une erreur s'est produite lors de l'appel à l'API : {e}")

def main() -> None:
    api_key = "votre_clé_api"
    client = OpenAIClient(api_key)

    prompt = "Bonjour, peux-tu m'expliquer le principe de la récursivité en programmation ?"
    try:
        response = client.send_prompt(prompt)
        print("Réponse du modèle :\n", response)
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()