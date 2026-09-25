import json
from urllib.parse import parse_qs
import importlib

routes_import = importlib.import_module('routes')
print(routes_import.routes)
routes = routes_import.routes

async def app(scope, receive, send):
    if scope['type'] != 'http':
        return

    path = scope['path']
    print('path', path)
    if path in routes:
        req_payload = {
            "path": path,
            "method": scope["method"],
            "query": parse_qs(scope["query_string"].decode('utf-8')),
            "headers": scope["headers"],
            # "body": scope["body"],
            # "cookies": scope["cookies"],
            # "ip": scope["ip"]
        }
        print(routes, path)
        data = routes[path](req_payload)
        print('data', data)
        if isinstance(data, dict):
            return_data = json.dumps(data).encode()
            type = b"application/json"  
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
    else:
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
  