from helpers.get_activation_token import get_email_info

# - Регистрируемся
# - Получаем активационный токен
# - Активируем
# - Заходим


def test_post_v1_account(account_api, login_api, mailhog_api):
    login = 'miv_test44'
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

    # Получить активационный токен
    token = get_email_info(login, response)
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




