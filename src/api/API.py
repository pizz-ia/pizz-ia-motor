import base64
import requests

class APIClient():

    def __init__(self, url):
        self.url = url
    
    def predict(self, img_path):
        data = open(img_path, "rb").read()
        encoded = base64.b64encode(data)
        r = requests.post(f'{self.url}/pizza-treatment', data = {'imageBase64': encoded})
        print(r.body)