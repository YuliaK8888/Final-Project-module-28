import time
from pages.footer_main_page import RulesPage, BusinessPage, AboutVkPage, DevelopersPage, UkrainianPage, EnglishLanguagePage, AllLanguagesPage


def test_rules_button(driver):
    rules_page = RulesPage(driver)
    rules_page.visit()
    rules_page.rules_button_load()
    time.sleep(2)
    rules_page.rules_button_click()
    time.sleep(2)
    assert rules_page.rules_page_open().is_displayed()


def test_business_button(driver):
    bsn_page = BusinessPage(driver)
    bsn_page.visit()
    bsn_page.business_button_load()
    time.sleep(2)
    bsn_page.business_button_click()
    time.sleep(7)
    assert bsn_page.business_page_open().is_displayed()


def test_about_vk_button(driver):
    vk_page = AboutVkPage(driver)
    vk_page.visit()
    vk_page.about_vk_button_load()
    time.sleep(2)
    vk_page.about_vk_button_click()
    time.sleep(5)
    assert vk_page.about_vk_page_open().is_displayed()


def test_developers_button(driver):
    dev_page = DevelopersPage(driver)
    dev_page.visit()
    dev_page.developers_button_load()
    time.sleep(2)
    dev_page.developers_button_click()
    time.sleep(5)
    assert dev_page.developers_page_open().is_displayed()


def test_ukrainian_language_button(driver):
    ukr_page = UkrainianPage(driver)
    ukr_page.visit()
    ukr_page.ukrainian_language_button_load()
    time.sleep(2)
    ukr_page.ukrainian_language_button_click()
    time.sleep(2)
    assert ukr_page.ukrainian_language_page_open().is_displayed()


def test_english_language_button(driver):
    eng_page = EnglishLanguagePage(driver)
    eng_page.visit()
    eng_page.english_language_button_load()
    time.sleep(2)
    eng_page.english_language_button_click()
    time.sleep(2)
    assert eng_page.english_language_page_open().is_displayed()


def test_all_languages_button(driver):
    all_lang_page = AllLanguagesPage(driver)
    all_lang_page.visit()
    all_lang_page.all_languages_button_load()
    time.sleep(2)
    all_lang_page.all_languages_button_click()
    time.sleep(2)
    assert all_lang_page.all_languages_page_open().is_displayed()