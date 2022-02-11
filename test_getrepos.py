import unittest
import json
import requests
from requests.auth import HTTPBasicAuth
from getrepo import get_data, username, token


class TestGetRepo(unittest.TestCase):
    maxDiff = None

    def test_sort_stars(self):
        data = get_data("calc", "", "stars", "desc", 1)["items"][0]["name"]
        test_res = requests.get("https://api.github.com/search/repositories?q=calc&language=&sort=stars&order=desc&per_page=1",
                                auth=HTTPBasicAuth(username, token))
        expected_data = json.loads(test_res.text)["items"][0]["name"]
        self.assertEqual(data, expected_data, msg="Failed on sort by stars test!")
    
    def test_sort_updated(self):
        data = get_data("piradoba", "python", "updated", "asc", 1)["items"][0]["name"]
        test_res = requests.get("https://api.github.com/search/repositories?q=piradoba&language=&sort=stars&order=desc&per_page=2",
                                auth=HTTPBasicAuth(username, token))
        expected_data = json.loads(test_res.text)["items"][0]["name"]
        self.assertEqual(data, expected_data, msg="Failed on sort updated test!")

    def test_static_json(self):
        data = get_data("tetris", "js", "stars", "desc", 1)["items"][0]["name"]
        with open('jsonTest/response.json', "r") as test_res:
            expected_data = json.loads(test_res.read())["items"][0]["name"]
        self.assertEqual(data, expected_data, msg="Failed on static json test!")


if __name__ == '__main__':
    unittest.main()
