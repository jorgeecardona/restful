
class BaseGateway(object)
    """
    Base Gateway
    ============

    This model deals with the interaction between the user and the api. 
    It basically translate the info from the outside world to the inner api.
    
    """

class LibraryGateway(BaseGateway):
    """
    Library Gateway
    ===============

    When we use the api from a library this is how we interact with it.

    There is a big difference in the way an http client make requests and how 
    a program using the library make requests. Basically some things with the 
    library are just set up at the beginning, in general we want to do something
    like this:

        import MyApi

        api = MyApi(user='myself', credential='topsecret')

        document = api.documents.create(name='Top secret document')
        document.content = "asadsada"
        document.save()

        another_document = api.documents.get(name="Previous document")
        yet_another_document = api.documents.get(id=1234)

    Look that the authentication process is setup just at the beginning and the rest
    are normal queries without any 'request' involved, and it actually seems ugly
    to ask for a request in any action, but the request is impotant to have control
    of how the user abuse of the api, the request then is created implicitely in
    this gateway.
        
    """

    
class HttpGateway(BaseGateway)
    """
    Http Gateway
    ============

    The more obvious entry point is the http one, we have to translate all the info 
    from a http request to the api, and the answer back.
    
    """
