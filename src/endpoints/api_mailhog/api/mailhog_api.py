import requests


class MailhogApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers


    def get_api_v2_messages(self, limit:int = 10, **kwargs):
        """
        Get Users emails
        :return:
        """
        params = {
            'limit': limit,
        }
        response = requests.get(f'{self.host}/api/v2/messages', params=params, verify=False, **kwargs)
        return response