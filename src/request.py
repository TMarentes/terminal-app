import requests
from urllib.request import urlopen
from urllib.request import Request
import json

class Requests:
    def __init__(self):
        pass

    def get_quote():
        data = requests.get('https://api.api-ninjas.com/v1/quotes?category=inspirational', headers={'X-Api-Key': 'r/EG6kiJC3Rc5V7pwcXsWQ==321MFqColfB9oTck'}).json()
        return(data)
    
    def get_uk():
        req = Request('http://pawster.cc/uk.json')
        req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
        response = urlopen(req)
        data_json = json.loads(response.read())
        return(data_json)
    
    def get_us():
        req = Request('http://pawster.cc/us.json')
        req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
        response = urlopen(req)
        data_json = json.loads(response.read())
        return(data_json)

