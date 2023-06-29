import requests

class Requests:
    def __init__(self):
        pass

    def get_quote():
        data = requests.get('https://api.api-ninjas.com/v1/quotes?category=inspirational', headers={'X-Api-Key': 'r/EG6kiJC3Rc5V7pwcXsWQ==321MFqColfB9oTck'}).json()
        return(data)

