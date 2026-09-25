import time
from melody.render import render

def index(req):
    return render('index.html', {'name': 'spj'}), 400

def time_api(req):
    if req["method"] == 'GET':
        return {"time":time.localtime(), "params": req["params"]}
    return {"error": "you cant do this little guy"}

routes = {
    '/': index,
    '/api/time/<int:id>': time_api, 
}