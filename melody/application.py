import json
from urllib.parse import parse_qs
import importlib
from bs4 import BeautifulSoup

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
    req_payload = {
            "path": path,
            "method": scope["method"],
            "query": parse_qs(scope["query_string"].decode('utf-8')),
            "headers": scope["headers"],
            "params": params
            # "body": scope["body"],
            # "cookies": scope["cookies"],
            # "ip": scope["ip"]
        }
    data = routes[endpoint](req_payload)

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
            "status": 200,
            "headers": [
                [b"content-type", type],
            ],
        })

    await send({
            "type": "http.response.body",
            "body": return_data,
        })
    return
  