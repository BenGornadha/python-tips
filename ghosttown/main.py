from openai import OpenAI
import json


class OpenAIClient:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key
        self.model = model
        self._client = OpenAI(
            api_key=api_key,  # This is the default and can be omitted
        )

    def send_prompt(self, prompt: str, temperature: float = 0.7) -> str:
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"Une erreur s'est produite lors de l'appel à l'API : {e}")


def load_api_key_from_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get("secret_value", "")
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")
    except json.JSONDecodeError:
        raise ValueError(f"Le fichier '{file_path}' contient un JSON invalide.")


def main() -> None:
    api_key_file = "secret_openai.json"  # Chemin vers le fichier contenant la clé API
    api_key = load_api_key_from_file(api_key_file)

    if not api_key:
        print("La clé API est introuvable ou vide. Vérifiez le fichier JSON.")
        return

    client = OpenAIClient(api_key)

    prompt = "Bonjour, peux-tu m'expliquer le principe de la récursivité en programmation ?"
    try:
        response = client.send_prompt(prompt)
        print("Réponse du modèle :\n", response)
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()

