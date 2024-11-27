from typing import List, Dict


class Customer:

    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.conversation_history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str) -> None:
        self.conversation_history.append({"role": role, "content": content})

    def get_history(self) -> List[Dict[str, str]]:
        return self.conversation_history.copy()
