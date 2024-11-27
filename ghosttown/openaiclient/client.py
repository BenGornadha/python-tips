from openai import OpenAI

from customer.customer import Customer


class OpenAIClient:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key
        self.model = model
        self._client = OpenAI(api_key=api_key)

    def send_prompt(self, customer: Customer, prompt: str, temperature: float = 0.7) -> str:
        customer.add_message("user", prompt)
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=customer.get_history(),
                temperature=temperature
            )
            assistant_response = response.choices[0].message.content
            customer.add_message("assistant", assistant_response)
            return assistant_response
        except Exception as e:
            raise RuntimeError(f"Une erreur s'est produite lors de l'appel à l'API : {e}")
