from selenium.webdriver.common.by import By
from element_action import ElementActions
from json_loaders_dir.load_browser_config import current_url
from json_loaders_dir.load_users_info import users


class IntroPage(ElementActions):
    def __init__(self, driver):
        ElementActions.__init__(self, driver)
        self.driver.get(current_url)

    def click_sign_in_button(self):
        self.click_element(By.CLASS_NAME, 'notSigned')

    def click_sign_up_button(self):
        self.click_element(By.CSS_SELECTOR, 'span[aria-label=להרשמה]')

    def send_name(self):
        self.enter_text(By.ID, 'ember1924', users.user_name(0))

    def assert_name(self):
        self.assert_element(By.ID, 'ember1924', users.user_name(0))

    def send_email(self):

        self.enter_text(By.ID, 'ember1931', users.user_email(0))

    def send_password(self):
        self.enter_text(By.ID, 'ember1937', users.password(0))

    def resend_password(self):
        self.enter_text(By.ID, 'ember1944', users.password(0))

    def click_checkbox(self):
        self.click_element(By.CLASS_NAME, 'fill')

    def click_submit(self):
        self.click_element(By.ID, 'ember1955')


