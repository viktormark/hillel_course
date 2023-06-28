from selenium import webdriver
from selenium.webdriver.common.by import By
from les19.pages.base import Base


class Elements(Base):

    def fill_name(self, text):
        self.driver.find_element(By.ID, "userName").send_keys(text)

    def fill_email(self, text):
        self.driver.find_element(By.ID, "userEmail").send_keys(text)

    def current_address(self, text):
        self.driver.find_element(By.ID, "currentAddress").send_keys(text)

    def permanent_address(self, text):
        self.driver.find_element(By.ID, "permanentAddress").send_keys(text)

    def click_submit(self):
        self.driver.find_element(By.ID, "submit").click()

    def click_check_boxes(self):
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button').click()

        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()

        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]').click()

        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]').click()

    def click_home_link(self):
        self.driver.find_element(By.XPATH, '//*[@id="simpleLink"]').click()