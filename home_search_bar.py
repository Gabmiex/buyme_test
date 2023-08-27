import time

from selenium.webdriver.common.by import By
from element_action import ElementActions


class HomePage(ElementActions):
    current_url = None

    def __init__(self, driver):
        ElementActions.__init__(self, driver)
        self.driver.get('https://buyme.co.il/')

    def click_on_amount(self):
        self.click_element(By.CSS_SELECTOR, 'div[data-ember-action="1075"]')

    def select_amount(self):

        self.click_element(By.CSS_SELECTOR, 'li[value="2"]')

    def click_on_region(self):
        self.click_element(By.CSS_SELECTOR, 'div[data-ember-action="1110"]')

    def select_region(self):
        self.click_element(By.CSS_SELECTOR, 'li[value="11"]')

    def click_on_category(self):
        self.click_element(By.CSS_SELECTOR, 'div[data-ember-action="1160"]')

    def select_category(self):
        self.click_element(By.CSS_SELECTOR, 'li[value="22"]')

    def click_on_submit(self):
        self.click_element(By.CSS_SELECTOR, 'a[rel="nofollow"]')
        time.sleep(3)
        # saves the current page state
        HomePage.current_url = self.driver.current_url

