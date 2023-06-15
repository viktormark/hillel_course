import allure
from selenium.webdriver.common.by import By


# pytest herokuapp.py -v --alluredir=allure-results
# allure serve allure-results

@allure.description("Add and Remove buttons")
def test_add_remove_elements(driver):
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a').click()

    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

    buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(buttons) == 2

    buttons[0].click()
    buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(buttons) == 1


@allure.description("Login Page")
@allure.severity(allure.severity_level.CRITICAL)
def test_authentication(driver):
    username = "tomsmith"
    password = "SuperSecretPassword!"
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    text = driver.find_element(By.XPATH, '//*[@id="flash"]')
    assert "You logged into a secure area!\n×" == text.text
