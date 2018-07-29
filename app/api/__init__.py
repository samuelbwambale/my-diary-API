from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .entries_resource import EntryListResource
from .entries_resource import EntryResource
#GET all entries or POST an entry
api.add_resource(EntryListResource,'/entries')
#GET or PUT or DELETE an entry
api.add_resource(EntryResource,'/entries/<int:entry_id>')

