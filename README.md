
Restful
=======

Create general restful api's, without http constraints, but with batteries for http.


Resources
=========

This is the basic model in django-rest, it came with the minimum to let you override almost all the settings.

The basic idea here lays in the fact that we're using HTTP verbs to interact with the resources in our system. Normally we Create, Delete, Modify and Retrieve any resource and we use HTTP verbs as POST, DELETE, PUT, GET for this. In some rare cases this verbs are note enough or just don't adjust to the create, delete, modify, retrieve model.

Then any resource has a way to map the HTTP verbs to the resource verbs and by default this match the usual way.



Taylored Resources
==================

django-rest came with a basic ResourceModel that it use the django orm as backend to create the resources.
