import time
import pytest
import allure

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from les19.pages.alerts import Alerts
from les19.pages.elements import Elements
from les19.pages.store import BookStore


# pytest test_demoqa.py
# allure serve allure-results
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class Creds:
    UserName = "viktormarkovetskyi"
    Password = "#Datatatatta668967-"


@allure.suite("Test Book Store")
class TestBookStore:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("test login")
    @allure.description("login as registered user")
    def test_login(self, driver):
        login = BookStore(driver)
        login.open("https://demoqa.com/login")
        login.input_username(Creds.UserName)
        login.input_password(Creds.Password)
        login.submit_login()

        assert driver.find_element(By.XPATH, '//*[@id="userName-value"]').text == Creds.UserName

    @allure.title("test add book to profile")
    def test_add_book(self, driver):
        # driver.get("https://demoqa.com/login")
        # driver.find_element(By.ID, "userName").send_keys(Creds.UserName)
        # driver.find_element(By.ID, "password").send_keys(Creds.Password)
        # driver.find_element(By.ID, "login").click()

        book_store = BookStore(driver)
        book_store.open("https://demoqa.com/login")
        book_store.input_username(Creds.UserName)
        book_store.input_password(Creds.Password)
        book_store.submit_login()
        time.sleep(0.6)

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        book_store.scroller()

        # driver.find_element(By.CSS_SELECTOR, ".show #item-2 > .text").click()  # Book Store
        book_store.click_book_store()

        # driver.find_element(By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a').click()  # Git Pocket Guide
        book_store.click_see_book()

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        book_store.scroller()

        # driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[2]/button').click()  # Add To Your Collection
        book_store.click_add_to_collection()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        # driver.get("https://demoqa.com/profile")
        book_store.open("https://demoqa.com/profile")

        assert driver.find_element(By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a').text == "Git Pocket Guide"


@allure.suite("Test Elements")
class TestElements:
    @allure.title("test text box")
    def test_text_box(self, driver):
        text_box = Elements(driver)

        name = "bizamok"
        email = "qysipifo@mailinator.com"

        text_box.open("https://demoqa.com/text-box")

        text_box.fill_name(name)

        text_box.fill_email(email)

        text_box.current_address("Est praesentium por")

        text_box.permanent_address("Architecto aut illum")

        text_box.click_submit()

        assert driver.find_element(By.XPATH, '//*[@id="name"]').text == f"Name:{name}"
        assert driver.find_element(By.XPATH, '//*[@id="email"]').text == f"Email:{email}"

    @allure.title("test check boxes")
    def test_check_box(self, driver):
        result = 'You have selected :\ndesktop\nnotes\ncommands'
        check_box = Elements(driver)
        check_box.open("https://demoqa.com/checkbox")
        check_box.click_check_boxes()

        assert driver.find_element(By.XPATH, '//*[@id="result"]').text == result

    @allure.title("test link")
    @allure.description("open link in new window")
    def test_links(self, driver):
        links = Elements(driver)
        links.open("https://demoqa.com/links")
        links.click_home_link()
        driver.switch_to.window(driver.window_handles[1])
        expected_url = "https://demoqa.com/"
        assert driver.current_url == expected_url


@allure.suite("Test Alerts")
class TestAlerts:
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Click Button to see alert")
    def test_see_alert(self, driver):
        alert = Alerts(driver)
        alert.open("https://demoqa.com/alerts")
        alert.click_button_to_see_alert()
        alert = driver.switch_to.alert
        assert alert.text == "You clicked a button"
        alert.accept()

    @allure.title("confirm box")
    @allure.description("On button click, confirm box will appear")
    def test_confirm_box(self, driver):
        alert = Alerts(driver)
        result = "You selected Ok"
        alert.open("https://demoqa.com/alerts")
        alert.confirm_box()
        alert = driver.switch_to.alert
        alert.accept()
        assert driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == result
