"""
DIP - 의존관계 역전 원칙
고수준 모듈은 저수준 모듈에 의존하면 안 된다. (추상화에 의존)
"""

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"[이메일 발송] {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)

if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    email_service.notify("안녕하세요!")
