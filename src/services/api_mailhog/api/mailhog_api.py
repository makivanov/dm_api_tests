import requests

from restclient.client import RestClient


class MailhogApi(RestClient):
    def get_api_v2_messages(self, limit:int = 10, **kwargs):
        """
        Get Users emails
        :return:
        """
        params = {
            'limit': limit,
        }
        response = self.get(path='/api/v2/messages', params=params, verify=False, **kwargs)
        return response