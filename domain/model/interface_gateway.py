from abc import ABC, abstractmethod

class AuthenticationService(ABC):
    @staticmethod
    @abstractmethod
    def login(username, password):
        pass
