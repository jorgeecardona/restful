from types import MetaType
from copy import copy

class Interface(object):
    """
    Interface
    =========

    Restful has (or I think it has) several key components:

    1) Unique addresses for each resource.
    2) Link between them.
    3) Reuse good standards.

    In any moment, any resource associated with an api object should be able to 
    have an unique address, something like:

    v1://users/1
    v1://users/
    ... so on...

    In such a way a resource can be uniquely identified even if we're not using http.

    Then any collection must have a name and any resource and id that uniquely identified
    them of the rest of collection and resources.

    Links between resources are accomplished in this way, and are stored just as links, 
    and resolved if needed just at the end.

    Reuse of good standards is a capability of the gateways.

    Random thoughts
    ---------------

    Any api needs an entry point, this should be that entry point.
    
    """    
    
    __metaclass__ = MetaType
    
    class Meta(object):
        collections = []

    def __init__(self, **kwargs):

        # Any kwarg will end in the meta of this instance.
        self._meta = copy.copy(self._meta)        
        self._meta.update(kwargs)

        # Create the collections.
        for collection_class in self._meta.collections:

            # Create instances of each collection.
            collection = collection_class(interface=self)

            # Store the collection in the api to avoid dynamic lookups.
            setattr(self, collection._meta.name, collection)
