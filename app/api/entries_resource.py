from flask_restplus import Resource, reqparse
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True,
                    help='Title must be a valid string')
parser.add_argument('description', type=str, required=True,
                    help='Description must be a valid string')

ENTRIES = []


class EntryResource(Resource):
    def get(self, entry_id):
        for entry in ENTRIES:
            if entry['entry_id'] == entry_id:
                return make_response(jsonify({
                    'status': 'success',
                    'entry': entry
                }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'Entry with this ID not found.',
        }), 404)

    def put(self, entry_id):
        data = parser.parse_args()
        for entry in ENTRIES:
            if entry['entry_id'] == entry_id:
                entry["title"] = data['title']
                entry["description"] = data['description']
                return make_response(jsonify({
                    'status': 'success',
                    'message': 'Entry edited successfully.',
                }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'Entry with this ID not found.',
        }), 404)

    def delete(self, entry_id):
        for entry in ENTRIES:
            if entry['entry_id'] == entry_id:
                ENTRIES.remove(entry)
                return make_response(jsonify({
                    'status': 'success',
                    'message': 'Entry deleted.'
                }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'Entry with this ID not found.',
        }), 404)


class EntryListResource(Resource):
    def get(self):
        return make_response(jsonify({'entries': ENTRIES}), 200)

    def post(self):
        data = parser.parse_args()
        title = data['title']
        description = data['description']
        if title.strip() == "":
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Title can not be empty.'}), 400)

        if len(title.strip()) < 4:
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Title should be at least 4 characters long.'}), 400)

        if description.strip() == "":
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Description can not be empty.'}), 400)

        if len(description.strip()) < 6:
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Sescription should be at least 6 characters long.'}), 400)
        for entry in ENTRIES:
            if entry['title'] == title:
                return make_response(jsonify({
                    'status': "Failed",
                    'message': 'Entry with same title already exists!',
                }), 400)
        entry = {
            "entry_id": len(ENTRIES)+1,
            "title": title,
            "description": description
        }
        try:
            ENTRIES.append(entry)
            return make_response(jsonify({
                'status': "success",
                'message': 'Entry successfully created!',
            }), 201)
        except Exception as err:
            return {'message': '{}'.format(err)}, 500
            