from selenium.webdriver.common.by import By
from les19.pages.base import Base


class BookStore(Base):
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login")
    BOOK_STORE = (By.CSS_SELECTOR, ".show #item-2 > .text")
    BOOK = (By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a')
    ADD_BOOK = (By.XPATH, "//*[contains(text(),'Add To Your Collection')]")
    ASSERT_NAME = (By.XPATH, '//*[@id="userName-value"]')
    ASSERT_BOOK_NAME = (By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a')

    def input_username(self, text):
        # self.driver.find_element(*self.USERNAME).send_keys(text)
        self.find(*self.USERNAME).send_keys(text)
        return self

    def input_password(self, text):
        self.find(*self.PASSWORD).send_keys(text)
        return self

    def submit_login(self):
        self.find(*self.LOGIN).click()

    def click_book_store(self):
        self.find(*self.BOOK_STORE).click()

    def click_see_book(self):
        self.find(*self.BOOK).click()

    def click_add_to_collection(self):
        self.find(*self.ADD_BOOK).click()

    def scroller(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def assert_name(self):
        return self.find(*self.ASSERT_NAME).text

    def assert_book_name(self):
        return self.find(*self.ASSERT_BOOK_NAME).text
