from fields import BaseField


class Struct(object):
    def __init__(self, **entries): 
        self.__dict__.update(entries)

    def update(self, values):
        self.__dict__.update(values)

    def __str__(self):

        pairs = ["%s=%s" % (k, v) for k,v in self.__dict__.items()]
        
        return "<Meta: %s >" % (' '.join(pairs))


class MetaType(type):
    """
    This type simply take a Meta defined in the class and creates a _meta
    based on its infor and its ancestors.
    """
    
    def __new__(cls, name, bases, attrs):

        # Empty meta.
        meta = Struct()
                
        # Add parents metas.
        for base in bases:
            if hasattr(base, '_meta'):
                meta.__dict__.update(vars(base._meta))
                    
        if 'Meta' in attrs:
            for name in vars(attrs['Meta']):
                if not name.startswith('_'):
                    setattr(meta, name, getattr(attrs['Meta'], name))

        # Look up for fields.
        if not hasattr(meta, 'fields'):
            setattr(meta, 'fields', {})

        # Walk through the attributes looking for fields.
        delete_this_attrs = []
        for attr in attrs:
            if not attr.startswith('_'):
                # Maybe a field :)
                if isinstance(attrs[attr], BaseField):
                    meta.fields[attr] = attrs[attr]
                    delete_this_attrs.append(attr)

        # Delete the used attrs.
        for attr in delete_this_attrs:
            attrs.pop(attr)
                    
        # Add to attrs.
        attrs['_meta'] = meta
            
        return super(MetaType, cls).__new__(cls, name, bases, attrs)            

    def __init__(self, *args, **kwargs):
        super(MetaType, self).__init__(*args, **kwargs)
