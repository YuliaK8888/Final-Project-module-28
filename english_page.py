from pages.main_page import MainPage
from settings import *
import selenium


class EnglishPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.english_switch = None

    def english_switch_load(self):
        self.english_switch = self.driver.find_element_by_xpath("//*[contains(text(), 'Switch to English')]")
        self.english_switch.click()

    def get_english_language(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'About VK')]")

