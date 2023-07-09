# .\cm.exe selenoid start
# .\cm.exe selenoid-ui start
import time

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "113.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True
        }
    }
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_text_input(driver):
    driver.get("https://www.google.com.ua/")
    text = driver.title
    time.sleep(10)
    assert text == "Google"
