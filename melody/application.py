import json
import importlib
from bs4 import BeautifulSoup
from melody.request import Request

routes_import = importlib.import_module('routes')
print(routes_import.routes)
routes = routes_import.routes

from werkzeug.routing import Map, Rule

route_map = Map([
    Rule(route, endpoint=route) for route in routes.keys()
    ])

def is_html(text):
    return bool(BeautifulSoup(text, "html.parser").find())

async def app(scope, receive, send):
    print('map', route_map)
    adapter = route_map.bind('http://127.0.0.1:8000/')

    if scope['type'] != 'http':
        return

    path = scope['path']
    try:
        endpoint, params = adapter.match(path)
    except:
        await send({
                    "type": "http.response.start",
                    "status": 404,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                })
        
        await send({
                    "type": "http.response.body",
                    "body": b"Not Found",
                })
        return
  
    data = routes[endpoint](Request(scope, params))
    data, status = data if isinstance(data, tuple) else (data, 200)

    if isinstance(data, dict):
        return_data = json.dumps(data).encode()
        type = b"application/json"  
    elif is_html(data):
        return_data = str(data).encode()
        type=b"text/html"
    else:
        return_data = str(data).encode()
        type = b"text/plain"
    await send({
            "type": "http.response.start",
            "status": status,
            "headers": [
                [b"content-type", type],
            ],
        })

    await send({
            "type": "http.response.body",
            "body": return_data,
        })
    return
  