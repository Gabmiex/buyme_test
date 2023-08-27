from selenium.webdriver.common.by import By
from element_action import ElementActions
from json_loaders_dir.load_receiver_info import receivers
from json_loaders_dir.load_users_info import users
from business_listings_page import Business


class SenderReceiver(ElementActions):
    IMAGE_PATH = 'C:/Users/Gabrielle/PycharmProjects/bymesite_test/image/gift.jpg'

    def __init__(self, driver):
        ElementActions.__init__(self, driver)
        self.driver.get(Business.current_url)

    # todo functions for the step one of the page --(https://buyme.co.il/money/20620?price=199)--(Business.current_url)
    def receiver_name(self):
        self.enter_text(By.ID, 'ember1376', users.user_name(0))

    def click_on_event(self):
        self.click_element(By.CSS_SELECTOR, 'div[data-ember-action="1806"]')

    def select_event(self):
        self.click_element(By.ID, 'ember1808')

    def remove_text_filler(self):
        self.clear_text(By.CSS_SELECTOR, 'textarea[data-parsley-group="voucher-greeting"]')

    def send_greeting(self):
        self.enter_text(By.CSS_SELECTOR, 'textarea[data-parsley-group="voucher-greeting"]', receivers.receiver_greeting(0))

    def upload_image(self):
        self.enter_text(By.CSS_SELECTOR, 'input[type="file"]', SenderReceiver.IMAGE_PATH)

    def click_on_submit(self):
        self.click_element(By.CSS_SELECTOR, 'button[type="submit"]')

    # todo functions for the step two of the page -- (https://buyme.co.il/money/20620?price=199&step=2) --
    def click_on_sms(self):
        self.click_element(By.CSS_SELECTOR, 'svg[gtm="method-sms"]')

    def receiver_phone_number(self):
        self.enter_text(By.ID, 'sms', '0533300767')

    def sender_name(self):
        self.enter_text(By.ID, 'ember1881', 'Gabriel')

    def sender_phone_number(self):
        self.enter_text(By.ID, 'ember1902', '0526891507')

    def click_on_continue(self):
        self.click_element(By.ID, 'ember1886')

    def enter_user_name(self):
        self.enter_text(By.CSS_SELECTOR, 'input[type="email"]', users.user_email(0))

    def enter_user_password(self):
        self.enter_text(By.CSS_SELECTOR, 'input[type="password"]', users.password(0))

    def click_on_login(self):
        self.click_element(By.CSS_SELECTOR, 'button[type="submit"]')
