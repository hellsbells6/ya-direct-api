# -*- coding: utf-8 -*-
from direct_api import DirectApi


def main():
    login, token = 'DIRECT_LOGIN', 'OAUTH_TOKEN'

    direct = DirectApi(login, token)  # Авторизируемся

    # Вызываем метод GetClientInfo для получения информации о клиенте
    response = direct.method(token, method='GetClientInfo', param=[login])
    print response

    # Вызываем метод GetCampaignParams для получения информации о кампании
    param = {
        'CampaignID': 111111
    }
    response = direct.method(token, method='GetCampaignParams', param=param)

    print response


if __name__ == '__main__':
    main()