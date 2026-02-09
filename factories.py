from faker import Faker
import random

fake = Faker()

def fake_note_dict():
    return {
        "title": fake.sentence(nb_words=4),
        "content": fake.paragraph(nb_sentences=random.randint(2, 5))
    }
