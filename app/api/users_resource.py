from flask_restplus import Resource, reqparse
from flask import jsonify, make_response
import re

users_list = []

class UserListResource(Resource):
    def get(self):
        return make_response(jsonify({'users': users_list}), 200)


class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True,
                    help='First name must be a valid string')
        parser.add_argument('last_name', type=str, required=True,
                    help='Last name must be a valid string')
        parser.add_argument('email', type=str, required=True,
                    help='Email must be a valid email')
        parser.add_argument('password', type=str, required=True,
                    help='Password must be a valid string')
        data = parser.parse_args()
        for user in users_list:
            if user['email'] == data['email']:
                return make_response(
                    jsonify({
                        'status': "Failed",
                        'message': 'Email Already registered!',
                        }), 400)
            else:
                if data['first_name'].strip() == "":
                    return make_response(jsonify({
                        'message': 'First name can not be empty.',
                        }), 400)
                if data['last_name'].strip() == "":
                    return make_response(jsonify({
                        'message': 'Last name can not be empty.',
                        }), 400)
                if not re.match("[^@]+@[^@]+\.[^@]+", data['email']):
                    return make_response(jsonify({
                        'message': 'Provided email is not a valid email address.',
                        }), 400)
                if data['password'].strip() == '':
                    return make_response(jsonify(
                        {'message': 'Password can not be empty .',
                        }), 400)
                if len(data['password']) < 4:
                    return make_response(jsonify(
                        {'message': 'Password must be atleast 4 characters in length.',
                        }), 400)
                user ={
                    "user_id": len(users_list)+1,
                    "first_name": data['first_name'],
                    "last_name": data['last_name'],
                    "email": data['email'], 
                    "password": data['password'],
                    }
                try:
                    users_list.append(user)
                    return make_response(jsonify({
                        'status': "success",
                        'message': 'User Successfully Created!!',
                        }), 201)
                except Exception as err:
                    return {'message': '{}'.format(err)}, 500 


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True,
                    help='Email must be a valid email')
        parser.add_argument('password', type=str, required=True,
                    help='Password must be a valid string')
        data = parser.parse_args()
        for user in users_list:
            if user['email'] == data['email']:
                if user['password'] == data['password']:
                    return make_response(jsonify({
                    'status': "success",
                    'message': 'Logged in',
                    }), 200)
                return make_response(jsonify({
                    'status': "failed",
                    'message': 'The password entered is incorrect.'
                    }), 401)
            return make_response(jsonify({
                'status': "failed",
                'message': 'The email entered is invalid or not registered.',
                }), 400)
        

class UserLogout(Resource):
    def post(self):
        return make_response(jsonify({
            'status': "success",
            'message':'Logged out successfully'}), 200)
        