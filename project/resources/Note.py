from flask import request
from flask_restful import Resource
from Model import db, Note,NoteSchema

notes_schema = NoteSchema(many=True)
note_schema = NoteSchema()

class NoteResource(Resource):
    def get(self):
        notes = Note.query.all()
        notes = notes_schema.dump(notes).data
        return notes ,200

    def post(self):
        print('Adding new note ')
        json_data = request.get_json(force=True)
        print(json_data)
        data,errors = note_schema.load(json_data)
        print(data,errors)

        note = Note(json_data['description'])
        db.session.add(note)
        db.session.commit()

        result = note_schema.dump(note).data

        return {"status":"success",'data':result},201
