import json

def test_post_v1_account(account_api, login_api, mailhog_api):
    login = 'miv_test9'
    password = '12345678'
    email = f'{login}@mail.ru'

    # Регистрация пользователя
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }
    response = account_api.post_v1_account(json_data=json_data)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'

    # Получить письмо
    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, 'Письма не были получены'

    # Получить активационный токон
    token = get_activation_token_by_login(login, response)
    assert token is not None, f'Токен для пользователя {login} не был получен'

    # Активация пользователя
    headers, response = account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, f'Пользователь {login} не был активирован'

    # Авторизация
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 200, f'Пользователь {login} не смог авторизоваться'


def get_activation_token_by_login(login, response):
    token = None
    for item in response.json()['items']:
        user_data = json.loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            break
    return token



