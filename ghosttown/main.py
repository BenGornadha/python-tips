import json

from customer.customer import Customer
from openaiclient.client import OpenAIClient


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

    customer_1 = Customer("client_001")
    customer_2 = Customer("client_002")

    client = OpenAIClient(api_key=api_key)
    prompt_1 = "Bonjour, je m'appelle Camille"
    print(f"Client 1 : {prompt_1}")
    response_1 = client.send_prompt(customer_1, prompt_1)
    print(f"Assistant : {response_1}")

    prompt_2 = "Bonjour, est-ce que tu sais comment je m'appelle ?"
    print(f"\nClient 2 : {prompt_2}")
    response_2 = client.send_prompt(customer_2, prompt_2)
    print(f"Assistant : {response_2}")

    prompt_3 = "Tu connais mon prénom ? "
    print(f"\nClient 1 : {prompt_3}")
    response_3 = client.send_prompt(customer_1, prompt_3)
    print(f"Assistant : {response_3}")


if __name__ == "__main__":
    main()
