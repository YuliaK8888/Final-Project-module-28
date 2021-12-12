from settings import *
import time
# import selenium
# from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_search_field(self):
        return self.driver.find_element_by_xpath("//*[@id='ts_input']")


class SearchPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_field = None

    def search_field_load(self):
        self.search_field = self.driver.find_element_by_xpath("//*[@id='ts_input']")

    def search_field_click(self):
        self.search_field.click()

    def search_field_send_word(self, word):
        self.search_field.clear()
        self.search_field.send_keys(word)
        time.sleep(2)
        self.search_field.send_keys(Keys.RETURN)

    def get_add_to_friends_list(self):
        return self.driver.find_elements_by_xpath('//*[contains(text(), "Добавить в друзья")]')

    def not_get_add_to_friends_list(self):
        return self.driver.find_element_by_xpath('//*[@id="no_results"]')


class RegistrationPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.registration_btn = None
        self.name_field = None
        self.surname_field = None
        self.day = None
        self.month = None
        self.year = None

    def registration_form_load(self):
        self.registration_btn = self.driver.find_element_by_xpath('//*[@class="FlatButton__content"]')
        self.name_field = self.driver.find_element_by_xpath('//*[@name="first_name"]')
        self.surname_field = self.driver.find_element_by_xpath('//*[@name="last_name"]')
        # self.day = self.driver.find_element_by_xpath('//*[@id="bday"]')
        # self.month = self.driver.find_element_by_xpath('//*[@id="bmonth"]')
        # self.year = self.driver.find_element_by_xpath('//*[@id="byear"]')

    def name_field_send_value(self, value):
        self.name_field.clear()
        self.name_field.send_keys(value)

    def surname_field_send_value(self, value):
        self.surname_field.clear()
        self.surname_field.send_keys(value)

    def registration_btn_click(self):
        self.registration_btn.click()

    def registration_load(self):
        return self.driver.find_element_by_xpath('//*[@name="phone"]')


class AllProductsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.all_products_button = None

    def all_products_button_load(self):
        self.all_products_button = self.driver.find_element_by_xpath("//*[@class='login_all_products_button']")

    def all_products_button_click(self):
        self.all_products_button.click()

    def all_products_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Другие приложения")]')


class FacebookPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.facebook_button = None

    def facebook_button_load(self):
        self.facebook_button = self.driver.find_element_by_xpath("//*[@class='fb-login-button']")

    def facebook_button_click(self):
        self.facebook_button.click()

    def facebook_page_open(self):
        return self.driver.find_element_by_xpath('//*[@id="u_0_0_Ni"]')


