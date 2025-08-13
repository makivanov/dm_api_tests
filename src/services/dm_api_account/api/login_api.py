import requests


class LoginApi:
    def __init__(self, host, headers:dict=None):
        self.host = host
        self.headers = headers

    def post_v1_account_login(self, json_data: dict, **kwargs):
        """
        Authenticate via credentials
        :param json_data:
        :return:
        """
        response = requests.post(url=f'{self.host}/v1/account/login', json=json_data, **kwargs)
        return response

    def delete_v1_account_login(self, headers: dict, **kwargs):
        """
        Logout as current user
        :param headers:
        :return:
        """
        response = requests.delete(url=f'{self.host}/v1/account/login', headers=headers, **kwargs)
        return response