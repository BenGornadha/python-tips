class NotificationSender:
    def send(self, message: str, method: str) -> str:
        if method == "email":
            return f"Sending email with message: {message}"
        elif method == "sms":
            return f"Sending SMS with message: {message}"
        raise ValueError("Unknown notification method")
