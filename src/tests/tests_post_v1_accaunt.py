import json

import requests

def test_post_v1_account(base_api_url, mail_url):
    login = 'miv_test4'
    password = '12345678'
    email = f'{login}@mail.ru'
    token = None

    # Регистрация пользователя
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post(f'{base_api_url}/v1/account', json=json_data)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'

    # Получить письмо
    params = {
        'limit': '10',
    }

    response = requests.get(f'{mail_url}/api/v2/messages', params=params, verify=False)
    assert response.status_code == 200, 'Письма не были получены'

    # Получить активационный токон
    for item in response.json()['items']:
        user_data = json.loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            print(f'{token=}')
            break
    assert token is not None, f'Токен для пользователя {login} не был получен'
    # Активация пользователя
    headers = {
        'accept': 'text/plain',
    }

    response = requests.put(f'{base_api_url}/v1/account/{token}', headers=headers)
    assert response.status_code == 200, f'Пользователь {login} не был активирован'

    # Авторизация

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post(f'{base_api_url}/v1/account/login', headers=headers, json=json_data)
    assert response.status_code == 200, f'Пользователь {login} не смог авторизоваться'