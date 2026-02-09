import requests
from faker import Faker
import random

API_URL = "http://127.0.0.1:8000/notes"
fake = Faker()

def generate_fake_note():
    return {
        "title": fake.sentence(nb_words=4),
        "content": fake.paragraph(nb_sentences=random.randint(2, 5))
    }

def seed(count=10):
    for _ in range(count):
        note = generate_fake_note()
        response = requests.post(API_URL, json=note)
        print(f"Added: {response.json()}")

if __name__ == "__main__":
    seed(10)
