from meta import MetaClass
import copy
from UserDict import UserDict


class ResourceBase(object):
    """
    General Resource Object
    =======================

    There  should be an etry point to the api, and this entry point 
    is defined in terms of requests, metnods data and then the rest 
    is made in inner bundled data.

    Also, simple batteries must be included, like authentication, 
    authorization, throttle, relations, documentation as playgrond.

    Meta attributes must be inherited from the base api to the resources
    
    """

    __metaclass__ = MetaClass

    class Meta(object):
        " Some nice defaults."
                
    def __init__(self, **kwargs):
        
        # Any kwarg will end in the meta of this instance.
        self._meta = copy.copy(self._meta)        
        self._meta.update(kwargs)
        
                        
    
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

    _counter = 1
    _storage = {}

    class Meta(object):
        actions = ['create', 'list']
    
    class ResourceNotFound(Exception):
        pass
    
    def __getitem__(self, value):
        """ 
        If we call this is because we want to lookup a particular
        resource in this collection.
        """

        # For new look up on the storage.
        if value in self._storage:
            return self._storage[value]

        raise self.ResourceNotFound
        
    def create(self, **kwargs):
        " Create a new resource."
                
        # Increase this counter, thread safe?
        cid = self._counter = self._counter + 1
        
        # Save in local storage.
        self._storage[cid] = self._meta['resource_class'](_cid=cid, **kwargs)
        
        return self._storage[cid]

    def retrieve(self, **kwargs):
        " Retrieve new resource."

        # If _cid in data use it!.
        if '_cid' in kwargs:
            try:
                return self._storage[kwargs['_cid']]
            except KeyError:
                raise self.ResourceNotFound("Resource not found.")
            
        # Ooops, that's the only thing we know how to do.
        raise self.ResourceNotFound("Resource not found.")

    def delete(self, **kwargs):
        " Basic delete a resource."

        if '_cid' in kwargs:
            return self._storage.pop(kwargs['_cid'])
        

class Resource(ResourceBase):
    """
    Resource
    ========

    A resource is basically a wrapper for the 'thing' that is useful in your
    app, whatever is a simple dict, a django orm object, whatever. 
    
    A resource is basically a piece of information sharing some 
    connection amount them and with the app itself. 
    
    It's the entry point from the outside world to the app.
    
    """

    def __init__(self, **kwargs):
        # Kwargs are not going to meta in here, we assume they are fields for our 
        # resource.

        self.__dict__ = kwargs
