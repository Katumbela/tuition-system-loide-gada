import requests

from domain.model.interface_gateway import AuthenticationService

class ApiService(AuthenticationService):
    @staticmethod
    def login(username, password):
        url = "http://localhost:8000/api/login"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        return None
