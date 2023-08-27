import time
from selenium.webdriver.common.by import By
from element_action import ElementActions
from home_search_bar import HomePage


class Business(ElementActions):

    current_url = None

    def __init__(self, driver):
        ElementActions.__init__(self, driver)
        self.driver.get(HomePage.current_url)

    def select_business(self):
        self.click_element(By.ID, 'ember1610')
        time.sleep(3)

    def send_amount(self):
        self.enter_text(By.ID, 'ember1882', '199')

    def click_on_submit(self):
        self.click_element(By.ID, 'ember1888')
        time.sleep(3)
        Business.current_url = self.driver.current_url
