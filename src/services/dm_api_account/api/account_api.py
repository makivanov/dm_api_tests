import requests


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data: dict, **kwargs):
        """
        Register new user
        :param self:
        :param json_data:
        :return:
        """
        response = requests.post(url=f'{self.host}/v1/account', json=json_data, **kwargs)
        return response

    def put_v1_account_token(self, token:str, **kwargs):
        """
        Activate registered user
        :param self:
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain',
        }
        response = requests.put(url=f'{self.host}/v1/account/{token}', headers=headers, **kwargs)
        return headers, response

    def put_v1_account_email(self, json_data: dict, **kwargs):
        """
        Change registered user email
        :param json_data:
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain',
        }
        response = requests.put(url=f'{self.host}/v1/account/email', json=json_data, headers=headers, **kwargs)
        print(response.request.body)
        return response
