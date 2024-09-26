from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending email with message: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending SMS with message: {message}")

class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending push notification with message: {message}")

class PidgeonNotificiation(Notification):
    def send(self, message:str):
        print(f"Sending Pidgeon with message: {message}")

class NotificationSender:
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    def send(self, message: str) -> None:
        self.notification.send(message)

