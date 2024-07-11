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


def set_random_ingredients():
    # Запрашиваем весь список ингредиентов и сортируем их по видам: булочки, соусы и начинки
    response = requests.get(f"https://stellarburgers.nomoreparties.site/api/ingredients")
    ingredients_data = response.json()["data"]
    buns = [ingredient["name"] for ingredient in ingredients_data if ingredient["type"] == "bun"]
    sauces = [ingredient["name"] for ingredient in ingredients_data if ingredient["type"] == "sauce"]
    mains = [ingredient["name"] for ingredient in ingredients_data if ingredient["type"] == "main"]

    # Выбираем по одному случайному ингредиенту: булочку, соус и начинку
    selected_bun = random.choice(buns)
    selected_sauce = random.choice(sauces)
    selected_main = random.choice(mains)

    # Возвращаем ингредиентов заказа: булочки, соуса и начинки
    return {
        "bun": selected_bun,
        "sauce": selected_sauce,
        "main": selected_main
    }
