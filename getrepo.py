import requests
import json
from requests.auth import HTTPBasicAuth

# Authentication
username = "davidcin" # Chane to your username
token = "token" # Change to your GitHub access token


def get_data(q, language="", sort="stars", order="desc", per_page=5):
    res = requests.get("https://api.github.com/search/repositories",
                       params={"q": f"{q} language:{language}", "sort": sort, "order": order, "per_page": per_page},
                       headers={"Accept": "application/vnd.github.v3+json"},
                       auth=HTTPBasicAuth(username, token))
    return json.loads(res.text)
