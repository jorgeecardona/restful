

class MetaData(dict):
    """
    MetaData
    =========

    Simple class to hold some meta-attributes of the resources.

    """
    
    def __str__(self):
        return "<Meta %s >" % (' '.join("%s=%s" % (k, v) for k,v in self.items()))


class MetaClass(type):
    """
    This type simply take a Meta defined in the class and creates a _meta
    based on its infor and its ancestors.
    """
    
    def __new__(cls, name, bases, attrs):

        # Empty meta.
        meta = MetaData()
                
        # Add parents metas.
        for base in bases:
            meta.update(getattr(base, '_meta', {}))

        # Search for own meta data.
        if 'Meta' in attrs:
            for name in vars(attrs['Meta']):
                if not name.startswith('_'):
                    meta[name] = getattr(attrs['Meta'], name)
                    
        # Add to attrs.
        attrs['_meta'] = meta
            
        return super(MetaClass, cls).__new__(cls, name, bases, attrs)            

    def __init__(self, *args, **kwargs):
        super(MetaClass, self).__init__(*args, **kwargs)
