import json
from bs4 import BeautifulSoup

def is_html(text):
    return bool(BeautifulSoup(text, "html.parser").find())

class Response:
    def __init__(self, data, response_type=None, status=200, headers={}, cookies={}):
        if response_type is not None:
            self.response_type = response_type
            self.response_data = (
            data if isinstance(data, bytes)
            else str(data).encode()
            )
        elif isinstance(data, dict):
            self.response_data = json.dumps(data).encode()
            self.response_type = b"application/json"  
        elif is_html(data):
            self.response_data = str(data).encode()
            self.response_type=b"text/html"
        else:
            self.response_data = str(data).encode()
            self.response_type = b"text/plain"
        self.status = status
        self.headers = headers
        self.cookies = cookies

def parse_response(response):
    print('type', type(response))
    if isinstance(response, Response):
        return response.response_data, response.response_type, response.status, response.headers, response.cookies
    temp_response = Response(response)
    print('t', temp_response.cookies)
    return temp_response.response_data, temp_response.response_type, temp_response.status, temp_response.headers, temp_response.cookies