from flask_restplus import Resource, reqparse
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
from app.api.models.entries import Entry
from app.api.resources.users_resource import UserLogin

now = datetime.datetime.now()
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True,
                    help='Title must be a valid string')
parser.add_argument('description', type=str, required=True,
                    help='Description must be a valid string')

class EntryResource(Resource):
    @jwt_required
    def get(self, entry_id):
        """ Method to retrieve a single entry of a user """
        ent = Entry(None, None, None)
        owner_id = get_jwt_identity()
        result = ent.get_single_entry_for_user(entry_id, owner_id)
        if not result:
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Entry not found.',
                }), 404)
        else:
            entry= {"entry_id":result[0], "owner_id":result[1], "title":result[2], "description":result[3], "create_date":result[4]}
            return make_response(jsonify({
                'status': 'success',
                'entry': entry
                }), 200)

    @jwt_required
    def put(self, entry_id):
        """ Method to update an entry """
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True,
                    help='Description must be a valid string')
        data = parser.parse_args()
        ent = Entry(None, None, None)
        owner_id = get_jwt_identity()
        result = ent.get_single_entry_for_user(entry_id, owner_id)
        if not result:
            return make_response(jsonify({
            'status': 'failed',
            'message': 'Entry not found.',
            }), 404)
        if result[4].strftime("%Y-%m-%d") == now.strftime("%Y-%m-%d"):
            if data["description"].strip() == "":
                return make_response(jsonify({
                    'status': 'failed',
                    'message': 'The new description can not be empty.'}), 400)

            if len(data["description"].strip()) < 4:
                return make_response(jsonify({
                    'status': 'failed',
                    'message': 'Description should be at least 4 characters long.'}), 400)
            ent.update_an_entry(entry_id, data['description'], owner_id)
            return make_response(jsonify({
                'status': 'success',
                'message': 'Entry edited successfully',
                }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'You can only edit an entry on the day it was created. Alternatively, you can add a new entry',
            }), 401)    

    @jwt_required      
    def delete(self, entry_id):
        """ Method to delete an entry """
        ent = Entry(None, None, None)
        owner_id = get_jwt_identity()
        result = ent.get_single_entry_for_user(entry_id, owner_id)
        if not result:
            return make_response(jsonify({
            'status': 'failed',
            'message': 'Entry with this ID not found.',
            }), 404)
        else:            
            ent.delete_an_entry(entry_id, owner_id)
            return make_response(jsonify({
            'status': 'success',
            'message': 'Selected entry has been deleted'
            }), 200)        
    

class EntryListResource(Resource):
    @jwt_required
    def get(self):
        """ Method to retrieve all entries of a particular user """
        owner_id = get_jwt_identity()
        ent = Entry(None, None, None)
        result = ent.get_all_entries(owner_id)
        if not result:
            return make_response(jsonify({
                'message': 'No entries. Please add entry.'
                }), 200)
        else:
            entries = []
            for row in result:
                entry= {"entry_id":row[0], "owner_id":row[1], "title":row[2], "description":row[3], "create_date":row[4]}
                entries.append(entry)
            return make_response(jsonify({
                'status': 'success',
                'entries': entries
                }), 200) 


    @jwt_required
    def post(self):
        """ Method to add an entry """
        data = parser.parse_args()
        title = data['title']
        description = data['description']
        if (title.strip() == "") or (description.strip() == ""):
            return make_response(jsonify({
                'status': 'failed',
                'message': 'The title or description can not be empty.'}), 400)
        if (len(title.strip()) < 4) or (len(description.strip()) < 4):
            return make_response(jsonify({
                'status': 'failed',
                'message': 'The title and description should be at least 4 characters long.'}), 400)
        ent = Entry(data['title'], data['description'], None)
        check_ent = ent.check_entry_with_title_exists(data['title'])
        if check_ent != 0:
            return make_response(jsonify({
                'status': "failed",
                'message': 'Entry with same title already exists!',
                }), 400)
                       
        owner_id = get_jwt_identity()
        entry = Entry(data['title'], data['description'], owner_id)
        entry.add_an_entry()
        return make_response(jsonify({
            'status': 'success',
            'message': 'Entry successfully created',
        }), 201)
            