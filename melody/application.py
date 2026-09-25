from .test import routes
import json

async def app(scope, receive, send):

    if scope['type'] != 'http':
        return
    print(scope['method'], scope['path'])

    path = scope['path']


    
    if path in routes:
        data = routes[path](scope)
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
  