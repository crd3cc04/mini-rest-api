# 📝 Mini REST API (FastAPI)

A lightweight REST API built with FastAPI demonstrating clean backend structure, CRUD operations, validation, seeding, and automated testing. This project is part of my engineering portfolio showcasing practical backend fundamentals, Python skills, and professional documentation.
---

## 🚀 Features

- CRUD operations for notes (`create`, `read`, `update`, `delete`)  
- Clean project structure (`app/`, `tests/`, `seed.py`) 
- Pydantic models for validation  
- In-memory storage for simplicity  
- Auto-generated Swagger UI (`/docs`)  
- Faker-powered randomized test data  
- Test-data factory for unit tests 
- Pytest test suite  

---

## 📁 Project Structure

```
mini-rest-api/
│
├── app/
│   └── main.py
│
├── logs/
│   └── system_report.log   # Auto‑generated
│
└── README.md
```

---

## 🔌 Endpoints

| Methods | Endpoints      | Description              |
|---------|----------------|--------------------------|
| GET     | `/notes`       | List all notes           |
| POST    | `/notes`       | Create a new note        |
| GET     | `/notes/{id}`  | Retrieve a single note   |
| PUT     | `/notes/{id}`  | Update an existing note  |
| DELETE  | `/notes/{id}`  | Delete a note            |

Swagger UI avaliable at:
`http://127.0.0.1:8000/docs` (127.0.0.1 in Bing)

---

## ▶️ Running the API
Start the server:

```bash
uvicorn app.main:app- --reload
```
Visit:
- API: `http://127.0.0.1:8000/notes`
- Docs: `http://127.0.0.1:8000/docs`

---

## 🌱 Seeding Test Data (Faker)
This project includes a `seed.py` script that generates randomized notes using Faker.

Run the API in one terminal:

```bash
uvicorn app.main:app --reload
```
Run the seed script in another terminal:

```bash
python3 seed.py
```
You can adjust the number of generated notes by editing:

```python
seed(10)
```

---

## 🧪 Running Tests
Tests use `pytest` and a custom Faker-powered test-data factory.

Run the test suite:

```bash
pytest -v
```
Includes tests:
- Create note
- List notes
- Dynamic note generation via factory

---

## 📌 Future Enhancements
- File-based storage option
- Pagination
- Authentication layer
- Dockerfile + containerization
- CI workflow for automated testing
