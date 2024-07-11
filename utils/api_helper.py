import requests
import random
import string


def generate_random_email():
    random_email = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_email}@yandex.ru"


def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string


def unique_user_data():
    return {
        "email": generate_random_email(),
        "password": generate_random_string(8),
        "name": generate_random_string(6)
    }


def create_user(payload):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
        return response
