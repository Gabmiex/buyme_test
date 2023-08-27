import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from intro_reg_page import IntroPage
from home_search_bar import HomePage
from business_listings_page import Business
from json_loaders_dir.load_browser_config import chrome_driver_patch, firefox_driver_patch, browser
from sender_receiver_info_page import SenderReceiver


class TestBuymePages(unittest.TestCase):
    def setUp(self):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(service=Service(chrome_driver_patch))

        elif browser == 'firefox':
            self.driver = webdriver.Firefox(service=Service(firefox_driver_patch))

        self.driver.implicitly_wait(10)

    def test_01_intro_reg_page(self):
        self.intro_page = IntroPage(self.driver)

        # todo clicking on sign-in button
        self.intro_page.click_sign_in_button()

        # todo clicking on sign-up button
        self.intro_page.click_sign_up_button()

        # todo entering name for registration
        self.intro_page.send_name()

        # todo entering email for registration
        self.intro_page.send_email()

        # todo entering and reentering password for registration
        self.intro_page.send_password()
        self.intro_page.resend_password()

        # todo clicking on checkbox to agree to terms
        self.intro_page.click_checkbox()

        # todo Checks if the name for registration is entered correctly
        self.intro_page.assert_name()

        # todo submit the details
        self.intro_page.click_submit()
        time.sleep(5)

    def test_02_home_search_bar_page(self):
        self.home_page = HomePage(self.driver)

        # todo clicking and selecting the amount of searching
        self.home_page.click_on_amount()
        self.home_page.select_amount()

        # todo clicking and selecting the region of searching
        self.home_page.click_on_region()
        self.home_page.select_region()

        # todo clicking and selecting the category of searching
        self.home_page.click_on_category()
        self.home_page.select_category()

        # todo submit the details
        self.home_page.click_on_submit()

        time.sleep(3)

    def test_03_business_listings_page(self):
        self.biz = Business(self.driver)

        # todo picking a business card
        self.biz.select_business()

        # todo selecting amount for the card
        self.biz.send_amount()

        # todo submitting the details
        self.biz.click_on_submit()
        time.sleep(3)

    def test_sender_receiver_info_page(self):
        self.sri_page = SenderReceiver(self.driver)

        # todo step one of the page -- (https://buyme.co.il/money/20620?price=199)

        # todo filling the receiver name
        self.sri_page.receiver_name()

        # todo clicking and selecting on the event
        self.sri_page.click_on_event()
        self.sri_page.select_event()

        # todo deleting text placeholder and filling with custom greeting
        self.sri_page.remove_text_filler()
        self.sri_page.send_greeting()

        # todo upload image
        self.sri_page.upload_image()

        # todo submitting the details
        self.sri_page.click_on_submit()
        time.sleep(3)

        # todo step two of the page -- (https://buyme.co.il/money/20620?price=199&step=2) --

        # todo clicking on the sms element and filling the phone number of the receiver
        self.sri_page.click_on_sms()
        self.sri_page.receiver_phone_number()

        # todo filling the name of the sender
        self.sri_page.sender_name()

        # todo filling the phone number of the sender
        self.sri_page.sender_phone_number()

        # todo submitting the details
        self.sri_page.click_on_continue()
        time.sleep(3)

        # todo filling the user name email
        self.sri_page.enter_user_name()

        # todo filling the user name password
        self.sri_page.enter_user_password()

        # todo clicking on the login button
        self.sri_page.click_on_login()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
