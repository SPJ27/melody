from melody import render
from melody import Response
from melody import cookie

def index(req):
    # return Response({'hello': 'world', 'cookies': req.cookies}, headers={'auth': True}, cookies={'session_id': '123123'})
    return Response({"cookies": req.cookies}, cookies=[cookie(name='kw', value='ssd')])

def new(req):
    try:
        return {"success": True}
    except:
        return {"success": False, "message": "Incomplete Data"}

routes = {
    '/': index,
    '/new': new 
}