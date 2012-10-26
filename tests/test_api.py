from unittest2 import TestCase
from restful.resource import Resource, Collection
from restful.api import Api
from restful.gateways import LibraryGateway


class User(Resource):
    pass


class UserCollection(Collection):
    class Meta(object):
        default_name = 'users'
        resource_class = User
        allowed_actions = ['create']
        
class MyApi(Api):
    class Meta(object):
        collections = [UserCollection]
        gateway = LibraryGateway()

        
class APITestCase(TestCase):
    
    def test_api_basic(self):
        " Basic usage of the api."

        # Create api entry point.
        api = MyApi(user='juan', password='rulfo')

        # Get a collection.
        api.users.create()
        
        # Create basic collection.
        users = UserCollection()

        # Create an user.
        user = users.create(username='pparamo')

        # Assert user.
        self.assertEqual(user.username, 'pparamo')

