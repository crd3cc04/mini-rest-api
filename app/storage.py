notes = []
next_id = 1

def add_note(note_data):
    global next_id
    note = { "id": next_id, **note_data }
    notes.append(note)
    next_id += 1
    return note

def get_all_notes():
    return notes

def get_note(note_id):
    return next((n for n in notes if n["id"] == note_id), None)

def update_note(note_id, data):
    note = get_note(note_id)
    if note:
        note.update(data)
    return note

def delete_note(note_id):
    global notes
    note = get_note(note_id)
    if note:
        notes = [n for n in notes if n["id"] != note_id]
    return note
