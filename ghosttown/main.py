import json

from customer.customer import Customer
from openaiclient.client import OpenAIClient


def load_api_key_from_file(file_path: str = "secret_openai.json"  ) -> str:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get("secret_value", "")
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")
    except json.JSONDecodeError:
        raise ValueError(f"Le fichier '{file_path}' contient un JSON invalide.")


def main() -> None:
    api_key = load_api_key_from_file()

    customer_1 = Customer("Camille")

    client = OpenAIClient(api_key=api_key)
    prompt_1 = "Bonjour, je m'appelle Camille"

    print(f"Client 1 : {prompt_1}")
    response_1 = client.send_prompt(customer_1, prompt_1)
    print(f"Assistant : {response_1}")



if __name__ == "__main__":
    # main()
    # Taux d'amélioration quotidien
    daily_growth_rate = 0.01

    # Nombre de jours
    days = 365

    # Calcul des intérêts composés
    final_value = (1 + daily_growth_rate) ** days
    print(final_value)