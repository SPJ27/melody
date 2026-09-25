from .test import routes
import json
from urllib.parse import parse_qs

async def app(scope, receive, send):

    if scope['type'] != 'http':
        return

    path = scope['path']

    matched_route = [route for route in routes if route.startswith(path)]
    
    if matched_route:
        req_payload = {
            "path": path,
            "method": scope["method"],
            "query": parse_qs(scope["query_string"].decode('utf-8')),
            "headers": scope["headers"],
            # "body": scope["body"],
            # "cookies": scope["cookies"],
            # "ip": scope["ip"]
        }
        
        data = routes[matched_route[0]](req_payload)
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
  