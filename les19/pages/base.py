class Base:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)
