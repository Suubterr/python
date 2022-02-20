import requests


class ApiCall:
    api_url = 'http://192.168.1.61/solar_api/v1/'

    def __init__(self, api_name, api_parameters):
        self.api_name = api_name
        self.api_parameters = api_parameters

    def call_api(self):
        return requests.get(self.api_url + self.api_name, params=self.api_parameters)
