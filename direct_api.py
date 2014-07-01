# -*- coding:utf-8 -*-

"""
@author: amureki
@contact: http://twitter.com/amureki
@license MIT License, see LICENSE file

Copyright (C) 2014
"""

import json
import urllib2

API_URL = 'https://api.direct.yandex.ru/live/v4/json/'


class DirectApi(object):
    def __init__(self, login=None, token=None):
        """
        :param login: Логин Direct
        :param token: Oauth-токен
        """

        self.login = login
        self.token = token

        if not login or not token:
            raise AuthorizationError(u'Введите логин и токен')

    def method(self, token, method, param=None):
        """ Использование методов API

        :param method: метод
        :param param: параметры
        """

        # 'GetClientInfo'

        data = {
            'method': method,
            'token': token,
            'locale': 'ru',
            'param': param
        }

        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        response = self.send_request(jdata)
        return response

    def send_request(self, jdata):
        response = urllib2.urlopen(API_URL, jdata).read()
        response = json.loads(response)

        if 'error_code' in response:
            error = ApiError(response)
            raise error
        else:
            return response['data']


class AuthorizationError(Exception):
    pass


class ApiError(Exception):
    def __init__(self, error):
        self.code = error['error_code']
        self.detail = error['error_detail'].encode('utf8')
        self.error = error['error_str'].encode('utf8')

    def __str__(self):
        return '[Error %s] %s (%s)' % (self.code, self.error, self.detail)