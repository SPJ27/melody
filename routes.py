from melody.render import render
from melody import Response

def index(req):
    return Response({'hello': 'world'}, status=401)

def new(req):
    try:
        return {"success": True}
    except:
        return {"success": False, "message": "Incomplete Data"}

routes = {
    '/': index,
    '/new': new 
}