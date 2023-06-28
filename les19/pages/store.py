from selenium import webdriver
from selenium.webdriver.common.by import By
from les19.pages.base import Base


class BookStore(Base):
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")

    def input_username(self, text):
        self.driver.find_element(*self.USERNAME).send_keys(text)

    def input_password(self, text):
        self.driver.find_element(*self.PASSWORD).send_keys(text)

    def submit_login(self):
        self.driver.find_element(By.ID, "login").click()

    def click_book_store(self):
        self.driver.find_element(By.CSS_SELECTOR, ".show #item-2 > .text").click()

    def click_see_book(self):
        self.driver.find_element(By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a').click()

    def click_add_to_collection(self):
        loc = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[2]/button'
        self.driver.find_element(By.XPATH, loc).click()

    def scroller(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
