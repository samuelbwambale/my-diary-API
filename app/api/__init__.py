from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .entries_resource import EntryListResource
from .entries_resource import EntryResource
api.add_resource(EntryListResource,'/entries')
api.add_resource(EntryResource,'/entries/<int:entry_id>')

from .users_resource import UserListResource
from .users_resource import UserRegister
from .users_resource import UserLogin
api.add_resource(UserListResource,'/users')
api.add_resource(UserRegister,'/auth/signup')
api.add_resource(UserLogin,'/auth/login')

