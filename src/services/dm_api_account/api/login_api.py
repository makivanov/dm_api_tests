import requests

from restclient.client import RestClient


class LoginApi(RestClient):
    def post_v1_account_login(self, json_data: dict, **kwargs):
        """
        Authenticate via credentials
        :param json_data:
        :return:
        """
        response = self.post(path='/v1/account/login', json=json_data, **kwargs)
        return response

    def delete_v1_account_login(self, headers: dict, **kwargs):
        """
        Logout as current user
        :param headers:
        :return:
        """
        response = self.delete(path='/v1/account/login', headers=headers, **kwargs)
        return response