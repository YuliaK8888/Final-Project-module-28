import json

import requests


class VKontakte:
    """апи библиотека к веб приложению Вконтакте"""

    def __init__(self):
        self.base_url = "https://api.vk.com/method/"

    def get_list_of_friends_online(self, access_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список идентификаторов друзей пользователя"""
        data = {'v': v,
                'user_id': user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'friends.getOnline', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_friends_get_recent(self, access_token: str, v: float) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список идентификаторов недавно добавленных друзей текущего пользователя"""
        v = {'v': v}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'friends.getRecent', headers=headers, params=v)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_friends_mutual(self, access_token: str, v: float, target_uid: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список идентификаторов общих друзей между парой пользователей"""
        data = {'v': v,
                'target_uid': target_uid}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'friends.getMutual', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_friends_app_users(self, access_token: str, v: float) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список идентификаторов друзей текущего пользователя, которые установили данное приложение"""
        v = {'v': v}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'friends.getAppUsers', headers=headers, params=v)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_users(self, access_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая расширенную информацию о пользователя"""
        data = {'v': v,
                'user_id': user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.get', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_users_followers(self, access_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая  список идентификаторов пользователей, которые являются подписчиками пользователя"""
        data = {'v': v,
                'user_id': user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.getFollowers', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_users_subscriptions(self, access_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список идентификаторов пользователей и публичных страниц, которые входят в список
        подписок пользователя."""
        data = {'v': v,
                'user_id': user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.getSubscriptions', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_search_of_users(self, access_token: str, v: float, q: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая список пользователей в соответствии с заданным критерием поиска"""
        data = {'v': v,
                'q': q}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.search', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_pages_version(self, access_token: str, v: float, version_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая текст одной из старых версий страницы"""
        data = {'v': v,
                'version_id': version_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'pages.getVersion', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_account_app_permissions(self, access_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        получая настройки текущего пользователя в данном приложении"""
        data = {'v': v,
                'user_id': user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'account.getAppPermissions', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_account_counters(self, access_token: str, v: float, filter: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате Json,
        возвращая ненулевые значения счетчиков пользователя"""
        data = {'v': v,
                'filter': filter}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'account.getCounters', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_friends_online_invalid_token(self, invalid_token: str, v: float, user_id: int) -> json:
        """Метод делает запрос к API сервера c использованием недействительного токена
        и возвращает статус запроса и результат в формате Json, который не должен
        вернуть список идентификаторов друзей пользователя"""
        data = {'v': v,
                'user_id': user_id}
        headers = {'invalid_token': invalid_token}

        res = requests.get(self.base_url + 'friends.getOnline', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_users_negative(self, access_token: str, v: float, negative_user_id: int) -> json:
        """Метод делает запрос к API сервера с использованием отрицательного значение user_id
        возвращает статус запроса и результат в формате Json,
        не возвращая расширенную информацию о пользователя, так как user_id только положительное число"""
        data = {'v': v,
                'negative_user_id': negative_user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.get', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_users_followers_negative(self, access_token: str, v: float, letter_user_id: int) -> json:
        """Метод делает запрос к API сервера , используя буквенное значение user_id
        и возвращает статус запроса и результат в формате Json,
        не возвращая  список идентификаторов пользователей, которые являются подписчиками пользователя, так
        как user_id только полож"""
        data = {'v': v,
                'letter_user_id': letter_user_id}
        headers = {'access_token': access_token}

        res = requests.get(self.base_url + 'users.getFollowers', headers=headers, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

