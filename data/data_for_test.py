import random
import string

TIME = '10'
WEIGHT = '100'
INGRIDIENT = 'сал'

def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    random_part = generate_random_string()
    return {
        "name": f"{random_part}",
        "surname": f"{random_part}",
        "username":f"user-{random_part}",
        "email": f"test-{random_part}@yandex.ru",
        "password": f"pass-{generate_random_string(8)}"
    }

def generate_recept_data():
    return {
        "name_recept": generate_random_string(8),
        "description": generate_random_string(20)
    }