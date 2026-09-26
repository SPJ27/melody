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
    example - {'error': 'unauthenticated'}, (optional) 401

3. templating
uses jinja2 templating in /templates/ folder in the root dir\
use render(filename, (optional) variables dictionary), (optional) status code to use templating

4. request

5. response
either return a dict, str or str with html. melody will map it automatically to json, text or html.
for more control over the response - use Response(data, response_type=, status=)
by default, the response type is autodetected, and status is 200
to send cookies, send it as cookies=[cookie(name='session_id', value='abc')]

6. render templates with response()
you can use response(render('index.html'), status=201)