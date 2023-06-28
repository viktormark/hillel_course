from selenium.webdriver.common.by import By
from les19.pages.base import Base


class Alerts(Base):
    def click_button_to_see_alert(self):
        self.driver.find_element(By.XPATH, '//*[@id="alertButton"]').click()

    def confirm_box(self):
        self.driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()

