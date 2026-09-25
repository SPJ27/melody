import time

def index(req):
    return {"hello": req["path"]}

def time_api(req):
    if req["method"] == 'GET':
        return {"time":time.localtime()}
    return {"error": "you cant do this little guy"}

routes = {
    '/': index,
    '/api/time/:id': time_api 
}