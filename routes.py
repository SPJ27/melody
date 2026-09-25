import time

def index(req):
    return {"hello": req["method"]}

def time_api(req):
    if req["method"] == 'GET':
        return {"time":time.localtime(), "id": req["params"]["id"]}
    return {"error": "you cant do this little guy"}

routes = {
    '/': index,
    '/api/time/<int:id>': time_api 
}