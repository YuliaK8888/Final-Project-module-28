import time
import json
from pages.main_page import*
from pages.english_page import EnglishPage
from pages.authorization_page import AutoPage
import pytest
import selenium


def test_visit(driver):
    main_page = MainPage(driver)
    main_page.visit()
    assert main_page.get_search_field().is_displayed()


def test_switch_to_english_language(driver):
    english_page = EnglishPage(driver)
    english_page.visit()
    english_page.english_switch_load()
    time.sleep(5)
    english_version = english_page.get_english_language()
    assert english_version.is_displayed()


def test_authorization(driver):
    auto_page = AutoPage(driver)
    auto_page.visit()
    auto_page.all_fields_load()
    auto_page.login_field_send_value("+79165390160")
    auto_page.password_field_send_value("Ych2508")
    time.sleep(2)
    auto_page.btn_enter.click()
    time.sleep(20)
    assert auto_page.get_authorization().is_displayed()


def test_negative_authorization(driver):
    auto_page = AutoPage(driver)
    auto_page.visit()
    auto_page.all_fields_load()
    auto_page.login_field_send_value("mail@gmail.com")
    auto_page.password_field_send_value("12235")
    time.sleep(2)
    auto_page.btn_enter.click()
    time.sleep(2)
    with pytest.raises(selenium.common.exceptions.NoSuchElementException):
        auto_page.get_authorization()


def test_button_search(driver):
    page = SearchPage(driver)
    page.visit()
    page.search_field_load()
    page.search_field_send_word('Казинцева')
    time.sleep(3)
    add_to_friends = page.get_add_to_friends_list()
    print(">>> total friends found: " + str(len(add_to_friends)))
    assert add_to_friends[0].is_displayed()


def test_negative_button_search(driver):
    page = SearchPage(driver)
    page.visit()
    page.search_field_load()
    page.search_field_send_word('&^%$#')
    time.sleep(3)
    not_to_friends = page.not_get_add_to_friends_list()
    assert not_to_friends.is_displayed()


def test_button_all_products(driver):
    prd_page = AllProductsPage(driver)
    prd_page.visit()
    prd_page.all_products_button_load()
    time.sleep(2)
    prd_page.all_products_button_click()
    time.sleep(2)
    page_open = prd_page.all_products_page_open()
    assert page_open.is_displayed()




