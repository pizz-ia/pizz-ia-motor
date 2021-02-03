import base64
import requests
import json

class APIClient():

    def __init__(self, url):
        self.url = url
    
    def predict(self, img_path):
        data = open(img_path, "rb").read()
        encoded = base64.b64encode(data)
        r = requests.post(f'{self.url}/pizza-treatment', json = {'imageBase64': encoded.decode('utf-8')})
        return r.json()['success'], r.json()['message']

    def last_predict(self):
        r = requests.get(f'{self.url}/pizza-treatment/last')
        return r.json()