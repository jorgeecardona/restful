from unittest2 import TestCase
from restful.resource import Resource, Collection

class User(Resource):
    pass


class UserCollection(Collection):
    class Meta(object):
        default_name = 'users'
        resource_class = User
        allowed_actions = ['create']


class CollectionTestCase(TestCase):
    
    def test_create_collection(self):
        " Create a collection."

        # Create basic collection.
        users = UserCollection()

        # Create an user.
        user = users.create(username='rulfo')

        # Assert user.
        self.assertEqual(user.username, 'rulfo')

