
from selenium.webdriver.common.by import By
from les19.pages.base import Base


class Elements(Base):
    NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    LINK = (By.XPATH, '//*[@id="simpleLink"]')
    CHECKBOX = (By.XPATH, "//*[contains(text(),'Home')]")
    ASSERT_NAME = (By.XPATH, '//*[@id="name"]')
    ASSERT_EMAIL = (By.XPATH, '//*[@id="email"]')
    ASSERT_BOX = (By.XPATH, '//*[@id="result"]')

    def fill_name(self, text):
        self.find(*self.NAME).send_keys(text)
        return self

    def fill_email(self, text):
        self.find(*self.EMAIL).send_keys(text)
        return self

    def current_address(self, text):
        self.find(*self.CURRENT_ADDRESS).send_keys(text)
        return self

    def permanent_address(self, text):
        self.find(*self.PERMANENT).send_keys(text)
        return self

    def click_submit(self):
        self.find(*self.SUBMIT).click()

    def click_check_boxes(self):
        self.find(*self.CHECKBOX).click()

    def click_home_link(self):
        self.find(*self.LINK).click()

    def assert_name(self):
        return self.find(*self.ASSERT_NAME).text

    def assert_email(self):
        return self.find(*self.ASSERT_EMAIL).text

    def assert_check_box(self):
        return self.find(*self.ASSERT_BOX).text
