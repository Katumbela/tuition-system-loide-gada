

from domain.entidades.entity import User
from domain.model.interface_gateway import AuthenticationService


def login(username, password):
    user_data = AuthenticationService.login(username, password)
    if user_data:
        user = User(**user_data)
        return user
    return None
