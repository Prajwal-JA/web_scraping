import requests
import json



API_KEY = "tcH82cR-Ef8C"
PROJECT_TOKEN = "tiQNEHM9aw0T"
RUN_TOKEN = "tLsZj-nJV_Wi"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',params={"api_key": API_KEY})
        self.data = json.loads(response.text)




    def get_commodity_data(self, Commodity):
        data = self.data["Commodity"]

        for content in data:
            if content['name'].lower() == Commodity.lower():
                return content['Price']

data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_commodity_data('Carrot'))

