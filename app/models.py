from pydantic import BaseModel

class Note(BaseModel):
    id: int | None = None
    title: str
    content: str
