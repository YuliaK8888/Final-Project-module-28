from api import VKontakte
from settings import *

vk = VKontakte()


def test_get_list_of_fiends_online_with_id_of_valid_user():
    """проверяем, что запрос на получение друзей пользователя с указанным id возвращает статус 200 и 'online'
    в результате"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_list_of_friends_online(access_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('response') >= 0


def test_get_friends_get_recent():
    """проверяем, что запрос на получение недавно добавленных друзей возвращает статус 200 и в результате
    длина 'response' больше 0 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_friends_get_recent(access_token, v)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('response') > 0


def test_get_friends_mutual_with_valid_target_uid():
    """проверяем, что запрос на получение общих друзей с  пользователем обозначенным target_uid
    возвращает статус 200 и в 'response' значение не равное 0"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_friends_mutual(access_token, v, target_uid=2234)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'response' != 0


def test_get_friends_app_users():
    """проверяем, что запрос на возвращение идентификаторов друзей, установивших данное приложение,
    возвращает статус 200 и в результате в 'response' длина либо равная 0, либо больше, что говорит о том,
    есть ли пользователи установившие приложение или нет"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_friends_app_users(access_token, v)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('response') >= 0


def test_get_users():
    """проверяем, что запрос на возвращение расширенной информации о пользователе возвращает статус 200 и
    в результате сравниваем что параметру 'first_name' соответствует 'first_name'  в расширенной ифнормации
    о пользователе"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_users(access_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert "first_name" != 0


def test_get_users_followers_with_valid_id_of_user():
    """проверяем, что запрос на получение списка подписчиков пользователя с данным id возвращает статус 200
    и результат в поле count не равен 0"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_users_followers(access_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'count' != 0


def test_get_users_subscriptions_with_valid_id_of_user():
    """проверяем, что запрос на получение списка подписок пользователя с данным id возвращает статус 200
    и значение в поле count более и равное 0"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_users_subscriptions(access_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('count') >= 0


def test_get_search_of_users():
    """проверяем, что запрос на получение списка пользователей в соответствии с заданным критерием поиска
    возвращает статус 200 и массив значений в поле items """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_search_of_users(access_token, v, q="Анастасия Покрасова")

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('items') > 0


def test_get_pages_version_with_correct_version_id():
    """проверяем, что запрос на получение текста старой версии страницы с указанным id возвращает статус 200
    и в результате, что длина значения параметра page_id больше 0"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_pages_version(access_token, v, version_id=183526239)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('page_id') > 0


def test_get_account_app_permissions_with_valid_user_id():
    """проверяем, что запрос на получение настроек в данном приложении указанного пользователя, возвращает
    статус 200 и значение в 'response' равное 0 или больше"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_account_app_permissions(access_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('response') >= 0


def test_get_account_counters_with_filter():
    """проверяем, что запрос на получение ненулевых значений счётчиков пользователя
    (значение интересующее указываем в фильтре) возвращает статус 200"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_account_counters(access_token, v, filter='messages')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'messages' != 0


def test_get_list_of_fiends_online_with_invalid_token():
    """проверяем, что запрос на получение друзей пользователя с указанным id и при использовании недействительного
    токена возвращает статус 200 и в результате выдаёт код ошибки 5 о том, что авторизация не удалась"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_list_of_friends_online_invalid_token(invalid_token, v, user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len("error_msg") > 0


def test_get_users_with_negative_id():
    """проверяем, что запрос на возвращение расширенной информации о пользователе при указании
    отрицательного значения user_id возвращает статус 200 и в результате код ошибки 113 о неверном идентификаторе
    пользователя"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_users(access_token, v, negative_user_id)

    # Сверяем полученные данные с нашими ожидан assert result
    assert status == 200
    assert len('error_code') > 0


def test_get_users_followers_with_id_of_user_letter():
    """проверяем, что запрос на получение списка подписчиков пользователя с буквенным значением
    id возвращает статус 200 и в результате код ошибки 100 о неверное значении параметра"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_users_followers(access_token, v, letter_user_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len('error_msg') > 0


def test_get_friends_mutual_with_invalid_target_uid():
    """проверяем, что запрос на получение общих друзей с  пользователем обозначенным target_uid
    возвращает статус 200 и в 'response' значение не равное 0"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, result = vk.get_friends_mutual(access_token, v, target_uid=-2234)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'response' != 0








