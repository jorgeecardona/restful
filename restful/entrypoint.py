
class BaseGateway(object)
    """
    Base Gateway
    ============

    This model deals with the interaction between the user and the api. 
    It basically translate the info from the outside world to the inner api.
    
    """


class HttpGateway(BaseGateway)
    """
    Http Gateway
    ============

    The more obvious entry point is the http one, we have to translate all the info 
    from a http request to the api, and the answer back.
    
    """
