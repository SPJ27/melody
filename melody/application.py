async def app(scope, receive, send):
    if scope['type'] != 'http':
        return

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            [b"content-type", b"application/json"],
        ],
    })

    await send({
        "type": "http.response.body",
        "body": b'{"hello": "world"}',
    })