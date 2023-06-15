import allure

from selenium.webdriver.common.by import By


# pytest test_globalsqa.py -v --alluredir=allure-results
# allure serve allure-results

@allure.suite("Test Customer Login")
class TestCustomerLogin:
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("test login")
    @allure.description("login Hermoine Granger")
    def test_login(self, driver):
        with allure.step("Открытие страницы входа"):
            driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

        with allure.step("Нажатие кнопки Customer Login"):
            driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()

        with allure.step("Выбор пользователя"):
            driver.find_element(By.ID, "userSelect").click()
            driver.find_element(By.XPATH, "//option[. = 'Hermoine Granger']").click()
            driver.find_element(By.CSS_SELECTOR, ".btn-default").click()

        with allure.step("Проверка имени"):
            text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/strong/span")
            assert "Hermoine Granger" == text.text

    @allure.title("test logout")
    def test_logout(self, driver):
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()
        driver.find_element(By.ID, "userSelect").click()
        driver.find_element(By.XPATH, "//*[@id=\"userSelect\"]/option[3]").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
        driver.find_element(By.XPATH, " /html/body/div[1]/div/div[1]/button[2]").click()
        expected_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
        assert driver.current_url == expected_url


@allure.suite("Test Withdrawn")
class TestWithdrawn:
    def test_successful_withdrawn(self, driver):
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()
        driver.find_element(By.ID, "userSelect").click()
        driver.find_element(By.XPATH, "//option[. = 'Hermoine Granger']").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/button[3]").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/input").send_keys("10")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/form/button").click()
        text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/span")
        assert "Transaction successful" == text.text

    def test_failed_withdrawn(self, driver):
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()
        driver.find_element(By.ID, "userSelect").click()
        driver.find_element(By.XPATH, "//option[. = 'Hermoine Granger']").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/button[3]").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/input").send_keys("966777")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/form/button").click()
        text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/span")
        assert "Transaction Failed. You can not withdraw amount more than the balance." == text.text


@allure.suite("Test Manager")
class TestManager:
    def test_add_customer(self, driver):
        name = "fname"
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
        driver.set_window_size(1451, 1020)
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child("
                            "3) > button").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.center > button:nth-child(1)").click()

        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.ng-scope > div > div > form > "
                            "div:nth-child(1) > input").send_keys(
            name)
        driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("lname")
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.ng-scope > div > div > form > "
                            "div:nth-child(3) > input").send_keys(
            "9090")
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.ng-scope > div > div > form > button").click()
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.ng-scope > div > div.ng-scope > div > div.center > button:nth-child(3)").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div/div/input").send_keys(name)
        text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]")
        assert name == text.text
