import requests
import json

API_KEY = "tcH82cR-Ef8C"
PROJECT_TOKEN = "tAFccxTbieh4"
RUN_TOKEN = "tqhRHRFYkTvx"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params = {"api_key": API_KEY})
data = json.loads(response.data)
print(data)