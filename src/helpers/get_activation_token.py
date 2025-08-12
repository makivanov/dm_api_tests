import json


def get_email_info(login, response):
    token = None
    for item in response.json()['items']:
        user_data = json.loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            break
    return token