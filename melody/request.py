from urllib.parse import parse_qs

class Request:
    def __init__(self, scope, params):
        print(scope)
        self.path = scope['path']
        self.method = scope['method']
        self.query = parse_qs(scope["query_string"].decode('utf-8'))
        self.headers = {key.decode('latin-1'): value.decode('latin-1')  for key, value in scope["headers"]}
        self.params = params
        self.scope = scope
        self.cookies = {}
        
        for cookie in self.headers.get('cookie', '').split(';'):
            if cookie == '':
                continue
            print('cookie', cookie)
            key, value = cookie.strip().split('=')
            self.cookies[key] = value