from unittest import TestCase

class BareCollectionTestCase(TestCase):

    def test_bare_collection(self):
        " Bare collection must have a natural behaviour. "

        from restful.resource import Collection, Resource

        # Add collection to it.
        users = Collection(resource_class=Resource)

        # Create an user.
        user = users.create(name='pedro')
        self.assertEqual(user.name, 'pedro')

        # Retrieve an user.
        user = users.retrieve(_cid=user._cid)        
        self.assertEqual(user.name, 'pedro')
        
        user = users[user._cid]
        self.assertEqual(user.name, 'pedro')

        # Delete an user.
        users.delete(_cid=user._cid)

        # Retrieve just deleted user must raise an error.
        with self.assertRaises(users.ResourceNotFound):
            users[user._cid]
