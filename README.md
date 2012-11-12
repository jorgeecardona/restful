
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
