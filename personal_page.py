from pages.main_page import MainPage


class FriendsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.friends_button = None

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

    def friends_button_load(self):
        self.friends_button = self.driver.find_element_by_xpath('//li[@id="l_fr"]/a')

    def friends_button_click(self):
        self.friends_button.click()

    def friends_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Поиск друзей")]')


class PhotoPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.photo_button = None

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

    def photo_button_load(self):
        self.photo_button = self.driver.find_element_by_xpath('//li[@id="l_ph"]/a')

    def photo_button_click(self):
        self.photo_button.click()

    def photo_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Добавить фотографии")]')


class MusicPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.music_button = None

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

    def music_button_load(self):
        self.music_button = self.driver.find_element_by_xpath('//li[@id="l_aud"]/a')

    def music_button_click(self):
        self.music_button.click()

    def music_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Моя музыка")]')


class VideoPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.video_button = None

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

    def video_button_load(self):
        self.video_button = self.driver.find_element_by_xpath('//li[@id="l_vid"]/a')

    def video_button_click(self):
        self.video_button.click()

    def video_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Интервью и шоу")]')


class ClipsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.clips_button = None

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

    def clips_button_load(self):
        self.clips_button = self.driver.find_element_by_xpath('//li[@id="l_svd"]/a')

    def clips_button_click(self):
        self.clips_button.click()

    def clips_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Для вас")]')


class GamesPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.games_button = None

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

    def games_button_load(self):
        self.games_button = self.driver.find_element_by_xpath('//li[@id="l_ap"]/a')

    def games_button_click(self):
        self.games_button.click()

    def games_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Мои игры")]')


class AdvertismentPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ad_button = None

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

    def ad_button_load(self):
        self.ad_button = self.driver.find_element_by_xpath('//li[@id="l_mk"]/a')

    def ad_button_click(self):
        self.ad_button.click()

    def ad_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Мои объявления")]')


class MiniAppsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.mini_apps_button = None

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

    def mini_apps_button_load(self):
        self.mini_apps_button = self.driver.find_element_by_xpath('//li[@id="l_mini_apps"]/a')

    def mini_apps_button_click(self):
        self.mini_apps_button.click()

    def mini_apps_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Популярное")]')


class MyPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.my_page_button = None

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

    def my_page_button_load(self):
        self.my_page_button = self.driver.find_element_by_xpath('//li[@id="l_pr"]/a')

    def my_page_button_click(self):
        self.my_page_button.click()

    def my_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Мои фотографии")]')


class ManagePage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.manage_button = None

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

    def manage_button_load(self):
        self.manage_button = self.driver.find_element_by_xpath('//li[@id="l_apm"]/a')

    def manage_button_click(self):
        self.manage_button.click()

    def manage_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Мои приложения")]')


class CallsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.calls_button = None

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

    def calls_button_load(self):
        self.calls_button = self.driver.find_element_by_xpath('//li[@id="l_ca"]/a')

    def calls_button_click(self):
        self.calls_button.click()

    def calls_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Позвонить друзьям")]')


class MessengersPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.messengers_button = None

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

    def messengers_button_load(self):
        self.messengers_button = self.driver.find_element_by_xpath('//li[@id="l_msg"]/a')

    def messengers_button_click(self):
        self.messengers_button.click()

    def messengers_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Объявления ВКонтакте")]')


class NewsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.news_button = None

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

    def news_button_load(self):
        self.news_button = self.driver.find_element_by_xpath('//li[@id="l_nwsf"]/a')

    def news_button_click(self):
        self.news_button.click()

    def news_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Истории")]')


class PodcastsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.podcasts_button = None

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

    def podcasts_button_load(self):
        self.podcasts_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_podcasts"]')

    def podcasts_button_click(self):
        self.podcasts_button.click()

    def podcasts_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Здесь вы будете видеть новостную ленту своих друзей.")]')


class CoronaVirusPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.coronavirus_button = None

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

    def coronavirus_button_load(self):
        self.coronavirus_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_coronavirus"]')

    def coronavirus_button_click(self):
        self.coronavirus_button.click()

    def coronavirus_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Коронавирус в мире. Новости:")]')


class FootballPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.football_button = None

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

    def football_button_load(self):
        self.football_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_football"]')

    def football_button_click(self):
        self.football_button.click()

    def football_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Чемпионат | Championat.com")]')


class RecommendationsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.recommendations_button = None

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

    def recommendations_button_load(self):
        self.recommendations_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_recommended"]')

    def recommendations_button_click(self):
        self.recommendations_button.click()

    def recommendations_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Комплекс парков «Дикие белки»")]')


class SearchPersonalPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_personal_button = None

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

    def search_personal_button_load(self):
        self.search_personal_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_search"]')

    def search_personal_button_click(self):
        self.search_personal_button.click()

    def search_personal_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Нет ни одной новости.")]')


class ReactionsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.reactions_button = None

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

    def reactions_button_load(self):
        self.reactions_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_likes"]')

    def reactions_button_click(self):
        self.reactions_button.click()

    def reactions_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Без названия")]')


class UpdatesPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.updates_button = None

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

    def updates_button_load(self):
        self.updates_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_updates"]')

    def updates_button_click(self):
        self.updates_button.click()

    def updates_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "добавила в друзья")]')


class CommentsPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.comments_button = None

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

    def comments_button_load(self):
        self.comments_button = self.driver.find_element_by_xpath('//*[@id="ui_rmenu_comments"]')

    def comments_button_click(self):
        self.comments_button.click()

    def comments_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Здесь будут показаны все новые комментарии к интересующим вас объектам.")]')


class ManagePage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.manage_button = None

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

    def manage_button_load(self):
        self.manage_button = self.driver.find_element_by_xpath('//li[@id="l_apm"]/a')

    def manage_button_click(self):
        self.manage_button.click()

    def manage_page_open(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Мои приложения")]')
