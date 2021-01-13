import requests
import curlify

from requests.auth import HTTPBasicAuth

from utils.list import chunk_list


class ExchangeApi(object):

    def __init__(self, user, credential, create_cart_uri, requests=requests):
        self.user = user
        self.credential = credential
        self.create_cart_uri = create_cart_uri
        self.requests = requests
    
    def create_cart(self, cart_name):
        request_body_as_dict = {
            "name": cart_name,
        }
        self.make_request(self.create_cart_uri, request_body_as_dict)
        
    @classmethod
    def _work_to_api_request_request_entry(cls, work):
        entry = {
            "id": work.get("id"),
            "quantity": work.get("quantity"),
        }

    def send_works(self, works, library_config_entry, chunk_size=1000):
        for chunk in chunk_list(works, chunk_size):
            request_body_as_dict = {
                "name": library_config_entry.cart_name,
                "items": len(chunk),
                "copies": sum([w.get("copies", 0) for w in chunk]),
                "values": {
                    "USD": sum([w.get("price", 0) for w in chunk]),
                },
                "Items": [self._work_to_api_request_request_entry(w)
                          for w in chunk],
            }
            self.make_request(url, request_body_as_dict)

    def make_request(self, url, data):
        headers = {
            "Content-Type": "application/json",
            # "User-Agent": "curl/7.64.0",
        }
        r = self.requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(self.user, self.credential))
        print(r.__dict__)

