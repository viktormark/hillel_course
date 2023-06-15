import time

import allure
import pytest
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# pytest uitestingplayground.py -v --alluredir=allure-results
# allure serve allure-results


@pytest.mark.skip()
def test_click(driver):
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id=\"overview\"]/div/div[2]/div[3]/h3/a").click()

    button = driver.find_element(By.XPATH, "//*[@id=\"badButton\"]")
    button.click()

    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"badButton\"]")))
    # button.click()
    time.sleep(1)

    button_color = button.value_of_css_property("background-color")
    expected_color = "rgba(33, 136, 56, 1)"
    assert button_color == expected_color


@allure.description("Record setting text into the input field and pressing the button.")
@allure.severity(allure.severity_level.BLOCKER)
def test_text_input(driver):
    name = "new name"
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id='overview']/div/div[2]/div[4]/h3/a").click()
    driver.find_element(By.XPATH, "//*[@id='newButtonName']").send_keys(name)
    button = driver.find_element(By.XPATH, "//*[@id='updatingButton']")
    button.click()
    assert button.text == name


@allure.description("Record 2 consecutive link clicks.")
def test_mouse_over(driver):
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id='overview']/div/div[4]/div[3]/h3/a").click()
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/a").click()
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/a").click()
    text = driver.find_element(By.XPATH, "//*[@id='clickCount']")
    assert text.text == "2"
