from pages.main_page import MainPage


class AutoPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_field = None
        self.password_field = None
        self.btn_enter = None

    def all_fields_load(self):
        self.login_field = self.driver.find_element_by_xpath("//*[@id='index_email']")
        self.password_field = self.driver.find_element_by_xpath("//*[@id='index_pass']")
        self.btn_enter = self.driver.find_element_by_xpath("//*[@id='index_login_button']")

    def login_field_send_value(self, value):
        self.login_field.clear()
        self.login_field.send_keys(value)

    def password_field_send_value(self, value):
        self.password_field.clear()
        self.password_field.send_keys(value)

    def btn_click(self):
        self.btn_enter.click()

    def get_authorization(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Моя страница')]")
