import requests

from ._exceptions import ApiError, NotExistsError


class ApiRequester:
    def __init__(self, url: str):
        self.url = url

    def get(self, params: dict | None = None) -> dict:
        if params:
            params = {k: v for k, v in params.items() if v} 
        
        response = requests.get(self.url, params)

        if response.status_code == 404:
            raise NotExistsError
        if response.status_code >= 300:
            raise ApiError(response.json()["error"])
        
        return response.json()
 