
class BaseField(object):
    pass

class IntegerField(BaseField):

    def __init__(self, description):
        " At this moment the field doesn't really know to which model belongs."        

        self.description = description

    def validate(self, value):
        " Validate a value."
        
        return isinstance(value, (int, long))

    def set(self, resource, name, value):
        " Set the value in a resource."

        if self.validate(value):
            return value
        else:
            raise TypeError("The field doesn't accept this data type.")            
