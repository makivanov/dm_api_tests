from helpers.get_activation_token import get_email_info

# - Регистрируемся
# - Получаем активационный токен
# - Активируем
# - Заходим
# - Меняем емейл
# - Пытаемся войти со старым токеном, получаем 403
# - На почте находим токен по новому емейлу для подтверждения смены емейла
# -.Активируем этот токен
# -  Логинимся

def test_put_v1_account_email(account_api, mailhog_api, login_api):
    login = 'miv_test42'
    password = '12345678'
    email = f'{login}@mail.ru'
    change_email = f'{login}_change@mail.ru'

    # # Регистрация пользователя
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
    token  = get_email_info(login, response)
    assert token is not None, f'Токен для пользователя {login} не был получен'

    # Активация токена
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

    #Смена емейла
    json_data = {
        'login': login,
        'password': password,
        'email': change_email,
    }
    response = account_api.put_v1_account_email(json_data=json_data)
    assert response.status_code == 200, f'Пользователь {login} не смог сменить email'

    # Авторизация со старого token
    headers, response = account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, f'Пользователь {login} смог авторизоваться со старым token'

    # Получить письмо
    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, 'Письма не были получены'

    # Получить активационный токон
    token = get_email_info(login, response)
    assert token is not None, f'Токен для пользователя {login} не был получен'

    # Активация нового токена
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