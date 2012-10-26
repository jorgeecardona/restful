
class ResourceBaseMeta(type):
    def __new__(cls, name, bases, attrs):

        # Anytime we get a Meta attrs, we're goint to get an instance and put it in _meta.
        if 'Meta' in attrs:
            attrs['_meta'] = attrs['Meta']()
        
        
        print name, bases, attrs

        return super(ResourceBaseMeta, cls).__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        super(ResourceBaseMeta, self).__init__(name, bases, attrs)
        
class ResourceBase(object):
    """
    General Resource Object
    =======================

    There  should be an etry point to the api, and this entry point is defined in terms of requests, metnods data and then the rest is made in inner bundled data.
    Also, simple batteries must be included, like authentication, authorization, throttle, relations, documentation as playgrond.

    We 

    """

    __metaclass__ = ResourceBaseMeta

    def dispatch_action(self, request):
        " Action dispatcher."

        # What action we want to perform?
        
        
    
    
class Collection(ResourceBase):
    """
    Collection of resources
    =======================

    A collection of resources share some aspects with the resources.

    Actions
    -------

    We can realize several actions with a collection:

    Create
    ......

    When one want to create a new resource inside a collection the way to go is calling
    `collection.create(...)` and we're going to get a new resource.

    Side processes
    --------------

    Normally we need to do some side processes when we interact with an api eg: throttle,
    authentication, authorization, validations et al.

    We're going to define a class to hold all this information, since is basically a
    request to the API.
    
    """

    def dispatch_action(self, request):
        " Dispatch a particular action."

        # Check what kind of action the client want to perform.
        action = request.action

        # We need to solve some question first:
        # 0) Dummy throttle.
        # 1) Who is the client?
        # 2) Can the client perform this action?
        # 3) Is the data at least type valid?
        # 4) Is the data 'business' valid?
        # 5) Smart throttle
        
        

        
    def create(self, **kwargs):
        " Create a new resource."

        # We need to build a request to the api.
        request = ApiRequest(action='create', data=kwargs)

        ## The user has permission to do this?
        ### User? what user?
        ## How many time has done this before?
        ## Are we sure the user is who it says to be?
        ## Can this action be performed given the request information?
        
        # Create resource.
        return self._meta.resource_class(**kwargs)
    

class Resource(ResourceBase):
    """
    Resource
    ======

    A resource is basically a piece of information sharing some 
    connection amount them and with the app itself. 
    
    It's the entry point from the outside world to the app.
    
    """

    def __init__(self, **kwargs):

        # Inner container of data.
        self._inner_data = kwargs

    def __getattr__(self, name):
        if name in self._inner_data:
            return self._inner_data[name]
        
        
     
