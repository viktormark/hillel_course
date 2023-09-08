import time

import multiprocessing
import os
from selenium import webdriver
from urllib.parse import urlparse


relative_directory = "skrins"

def get_domain_name(url):

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def take_screenshot(url):
    current_directory = os.getcwd()

    save_directory = os.path.join(current_directory, relative_directory)

    driver = webdriver.Chrome()
    driver.get(url)

    domain_name = get_domain_name(url)
    screenshot_filename = f"{domain_name}.png"

    screenshot_path = os.path.join(save_directory, screenshot_filename)

    driver.save_screenshot(screenshot_path)

    driver.quit()




if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.map(take_screenshot, ['https://duckduckgo.com/', "https://www.google.com.ua/", 'https://dou.ua/'])

