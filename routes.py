from melody.render import render

def index(req):
    return {"method": req.cookies}

def new(req):
    try:
        return {"success": True}
    except:
        return {"success": False, "message": "Incomplete Data"}, 400

routes = {
    '/<int:id>/hello/<string:world>': index,
    '/new': new 
}