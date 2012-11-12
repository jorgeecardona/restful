
RESTful
=======

[![Build Status](https://travis-ci.org/jorgeecardona/restful.png)](https://travis-ci.org/jorgeecardona/restful)

Create general RESTful api's, without http constraints, but with batteries for http.

First Milestone
===============

Create a basic library making an abstraction of what is good in a RESTful API but 
for non-http usage.

This includes a battery for plugin Django orm models, MongoDB, and Cassandra (pycassa).

Goals
=====

This is the basic list of goals for restful:

1) Be able to use it not only in http context but also as a library.

2) Batteries included for django orm.

3) Avoid problems with nose discovery.

4) Allow easy checking of permissions.

5) Keep the api as descriptive as possible

6) Automatic documentation.



Usage (for now)
===============

Basic usage of collections for now is likes this:

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
