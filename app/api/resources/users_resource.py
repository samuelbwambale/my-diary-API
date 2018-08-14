from flask_restplus import Resource, reqparse
from flask import jsonify, make_response
from datetime import timedelta
from flask_jwt_extended import create_access_token
import re
from app.api.models.users import User

class UserRegister(Resource):
    def post(self):
        """ Method to signup a user """
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
        if (data['first_name'].strip() == "") or (data['last_name'].strip() == "") or (data['email'].strip() == '') or (data['password'].strip() == ''):
            return make_response(jsonify({
                'status': 'failed',
                'message': 'The fistname or lastname or email or password can not be empty.'
                }), 400)
        if not re.match("[^@]+@[^@]+\.[^@]+", data['email']):
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Provided email is not a valid email address.'
                }), 400)
        if len(data['password']) < 4:
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Password must be atleast 4 characters in length.'
                }), 400)      
        user = User(data['first_name'], data['last_name'], data['email'],data['password'] )
        result = user.get_user_by_email(data['email'])  
        if result !=0:
            return make_response(
                    jsonify({
                        'status': "failed",
                        'message': 'This email is already used',
                        }), 400)
        try:
            user.add_user()
            return make_response(jsonify({
                'status': "success",
                'message': 'Account successfully created',
                }), 201)
        except Exception as err:
            return {'message': '{}'.format(err)}, 500 


class UserLogin(Resource):
    def post(self):
        """ Method to login a user and obtain a token """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True,
                    help='Email must be a valid email')
        parser.add_argument('password', type=str, required=True,
                    help='Password must be a valid string')
        data = parser.parse_args()

        usr = User(None, None,data['email'],data['password'] )
        row = usr.login_user(data['email'], data['password'])
        if row:
            expires = timedelta(minutes=60)
            user_id = row[0]
            token = create_access_token(identity=user_id, expires_delta=expires)
            
            return make_response(jsonify({
                'status': "success",
                'message': "Logged in",
                'Token'  : token
                }), 200)
        else:
            return make_response(jsonify({
                'status': "failed",
                'message': "Invalid username or password."
                }), 401)


class UserLogout(Resource):
    def post(self):
        """ Method to logout a user """
        return make_response(jsonify({
            'status': "success",
            'message':'Logged out successfully'}), 200)
        

class UserListResource(Resource):
    def get(self):
        """ Method to retrieve all exisiting users """
        usr = User(None, None, None, None )
        users = usr.get_all_users()
        if not users:
            return make_response(jsonify({
                'message': 'No users subscribed as yet',
                }), 200)
        else:
            user_lst = []
            for u in users:
                user= {"user_id":u[0], "first_name":u[1], "last_name":u[2], "email":u[3], "password":u[4]}
                user_lst.append(user)
            return make_response(jsonify({
                'status': 'success',
                'entry': user_lst
                }), 200)
