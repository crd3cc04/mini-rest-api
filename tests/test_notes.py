from fastapi.testclient import TestClient
from app.main import app
from .factories import fake_note_dict

client = TestClient(app)

def test_create_note():
    note = fake_note_dict()
    response = client.post("/notes", json=note)

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == note["title"]
    assert data["content"] == note["content"]

def test_list_notes():
    # Create a few notes
    for _ in range(3):
        client.post("/notes", json=fake_note_dict())

    response = client.get("/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 3
