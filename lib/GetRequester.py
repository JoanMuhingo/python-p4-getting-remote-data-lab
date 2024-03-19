import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content


    def load_json(self):
        response_body = self.get_response_body()
        try:
            response_text = response_body.decode('utf-8')  
            json_data = json.loads(response_text)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        