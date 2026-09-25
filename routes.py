import time

def index(req):
    return "<p>hi</p>"

def time_api(req):
    if req["method"] == 'GET':
        return {"time":time.localtime(), "params": req["params"]}
    return {"error": "you cant do this little guy"}

routes = {
    '/': index,
    '/api/time/<int:id>': time_api, 
    '/api/time/<int:id>/new/<string:name>': time_api 
}