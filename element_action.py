
class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, locator_value).click()

        except ValueError:
            self.driver.find_element(locator_type, locator_value).screenshot('element.png')

    def enter_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, locator_value).send_keys(text)

        except ValueError:
            self.driver.find_element(locator_type, locator_value).screenshot('element.png')

    def clear_text(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).clear()

    def assert_element(self, locator_type, locator_value, text):
        element = self.driver.find_element(locator_type, locator_value)
        try:
            assert element.text == text

        except AssertionError:
            print("AssertionError: Unexpected name")
