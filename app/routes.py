from fastapi import APIRouter, HTTPException
from .models import Note
from .storage import add_note, get_all_notes, get_note, update_note, delete_note

router = APIRouter()

@router.get("/notes")
def list_notes():
    return get_all_notes()

@router.post("/notes")
def create_note(note: Note):
    new_note = add_note(note.dict(exclude={"id"}))
    return new_note

@router.get("/notes/{note_id}")
def read_note(note_id: int):
    note = get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/notes/{note_id}")
def edit_note(note_id: int, note: Note):
    updated = update_note(note_id, note.dict(exclude={"id"}))
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

@router.delete("/notes/{note_id}")
def remove_note(note_id: int):
    deleted = delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}
