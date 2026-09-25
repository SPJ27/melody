1. Creating the basic app
Define all the routes in 

python``
routes = {
    "/": index,
    ...etc
}
``

2. Creating controllers
def index(req):
    return {} => returns json, "str" returns plain text, and use html tags to automatically detect html. 
    add a comma separated value to send status code.
    example - {'error': 'unauthenticated'}, 401