from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .resources.entries_resource import EntryListResource
from .resources.entries_resource import EntryResource
api.add_resource(EntryListResource,'/entries')
api.add_resource(EntryResource,'/entries/<int:entry_id>')

from .resources.users_resource import UserListResource
from .resources.users_resource import UserRegister
from .resources.users_resource import UserLogin
from .resources.users_resource import UserResource
api.add_resource(UserListResource,'/users')
api.add_resource(UserRegister,'/auth/signup')
api.add_resource(UserLogin,'/auth/login')
api.add_resource(UserResource,'/users/<int:user_id>')
