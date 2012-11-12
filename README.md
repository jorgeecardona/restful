
RESTful
=======

[![Build Status](https://travis-ci.org/jorgeecardona/restful.png)](https://travis-ci.org/jorgeecardona/restful)

Create general RESTful api's, without http constraints, but with batteries for http.

Acknowledge
===========

I have used some previous rest tools in django and I don't like them in some ways and love them in others, maybe this is going to be just one more piece in the chain, but I want to add my thoughts in this aspect.

I took some ideas from piston (jespern), tastypie (Daniel Lidnsey), and Backbone, and resources (Kenneth Reitz). Thank you!


First Milestone
===============

Create a basic library making an abstraction of what is good in a RESTful API but 
for non-http usage.

This includes a battery for plugin Django orm models, MongoDB, and Cassandra (pycassa).

Goals
=====

This is the basic list of goals for restful:

1) Keep the api as descriptive as possible

2) Batteries (no magic) included for django orm, mongoengine and pycassa.

3) Be able to use it not only in http context but also as a library.

4) Avoid problems with nose discovery.

5) Allow easy checking of permissions.

6) Automatic documentation.


RESTful's API
=============

Even this has an api. The basic objects are Collection and Resource bothr inherit from
a ResourceBase object that deals with the metadata defined for each one in Meta classes
in each definition.

For now, resources are schemeless, and no backend is defined yet. (Django orm comming.)

A Interface object is defined but with not too much thoughs about it, and is going to be
the main entry point for the api (not this one, the one you're building).

Collection
----------

TBD

Resource
--------

TBD

Interface
---------

TBD


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
