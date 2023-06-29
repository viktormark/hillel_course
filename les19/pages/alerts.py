from selenium.webdriver.common.by import By
from les19.pages.base import Base


class Alerts(Base):
    ALERT = (By.XPATH, '//*[@id="alertButton"]')
    CONFIRM = (By.XPATH, '//*[@id="confirmButton"]')
    ASSERT_ALERT_TEXT = (By.XPATH, '//*[@id="confirmResult"]')

    def click_button_to_see_alert(self):
        self.find(*self.ALERT).click()

    def confirm_box(self):
        self.find(*self.CONFIRM).click()

    def assert_alert(self):
        return self.find(*self.ASSERT_ALERT_TEXT).text
