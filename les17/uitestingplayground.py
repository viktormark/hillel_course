import time

from selenium.webdriver.common.by import By


# pytest uitestingplayground.py -v


def test_click(setup):
    driver = setup
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id=\"overview\"]/div/div[2]/div[3]/h3/a").click()
    button = driver.find_element(By.XPATH, "//*[@id=\"badButton\"]")
    button.click()
    time.sleep(1)
    button_color = button.value_of_css_property("background-color")
    expected_color = "rgba(33, 136, 56, 1)"
    assert button_color == expected_color


def test_text_input(setup):
    name = "new name"
    driver = setup
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id='overview']/div/div[2]/div[4]/h3/a").click()
    driver.find_element(By.XPATH, "//*[@id='newButtonName']").send_keys(name)
    button = driver.find_element(By.XPATH, "//*[@id='updatingButton']")
    button.click()
    assert button.text == name


def test_mouse_over(setup):
    driver = setup
    driver.get("http://uitestingplayground.com/")
    driver.find_element(By.XPATH, "//*[@id='overview']/div/div[4]/div[3]/h3/a").click()
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/a").click()
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/a").click()
    text = driver.find_element(By.XPATH, "//*[@id='clickCount']")
    assert text.text == "2"

