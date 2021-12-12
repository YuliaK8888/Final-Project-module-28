from settings import *
import time
from pages.main_page import MainPage


class RulesPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rules_button = None

    def rules_button_load(self):
        self.rules_button = self.driver.find_element_by_xpath('//*[contains(text(), "Правила")]')

    def rules_button_click(self):
        self.rules_button.click()

    def rules_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Правила пользования Сайтом ВКонтакте")]')


class BusinessPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.business_button = None

    def business_button_load(self):
        self.business_button = self.driver.find_element_by_xpath('//*[contains(text(), "Для бизнеса")]')

    def business_button_click(self):
        self.business_button.click()

    def business_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Подписаться")]')
        #return self.driver.find_element_by_xpath('//meta[@content="https://vk.com/biz"]')


class AboutVkPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.about_vk_button = None

    def about_vk_button_load(self):
        self.about_vk_button = self.driver.find_element_by_xpath('//*[contains(text(), "О ВКонтакте")]')

    def about_vk_button_click(self):
        self.about_vk_button.click()

    def about_vk_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Где мы работаем")]')


class DevelopersPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.developers_button = None

    def developers_button_load(self):
        self.developers_button = self.driver.find_element_by_xpath('//*[contains(text(), "Разработчикам")]')

    def developers_button_click(self):
        self.developers_button.click()

    def developers_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Товары")]')


class UkrainianPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ukrainian_language_button = None

    def ukrainian_language_button_load(self):
        self.ukrainian_language_button = self.driver.find_element_by_xpath('//*[contains(text(), "Українська")]')

    def ukrainian_language_button_click(self):
        self.ukrainian_language_button.click()

    def ukrainian_language_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "VK для мобільних пристроїв")]')


class EnglishLanguagePage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.english_language_button = None

    def english_language_button_load(self):
        self.english_language_button = self.driver.find_element_by_xpath('//*[contains(text(), "English")]')

    def english_language_button_click(self):
        self.english_language_button.click()

    def english_language_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "VK for mobile devices")]')


class AllLanguagesPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.all_languages_button = None

    def all_languages_button_load(self):
        self.all_languages_button = self.driver.find_element_by_xpath('//*[contains(text(), "все языки")]')

    def all_languages_button_click(self):
        self.all_languages_button.click()

    def all_languages_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Выберите ваш язык")]')
