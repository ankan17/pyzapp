import os
import sys
import time
import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PyWhatsApp():

    def __init__(self, path_to_profile, path_to_driver):
        os.environ['MOZ_HEADLESS'] = '1'
        self.profile = webdriver.FirefoxProfile(path_to_profile)
        self.path_to_driver = path_to_driver

        self.browser = webdriver.Firefox(self.profile, executable_path=self.path_to_driver)
        self.browser.get("https://web.whatsapp.com/")
        self.wait = WebDriverWait(self.browser, 600)


    def sendMessage(self, friend, message):
        x_arg = '//span[contains(@title,' + friend + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        inp_xpath = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
        input_box = self.wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        input_box.send_keys(message + Keys.ENTER)

    def __del__(self):
        time.sleep(5)
        self.browser.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("friend")
    parser.add_argument("message")
    args = parser.parse_args()

    # Replace the corresponding variables here
    path_to_profile = '/home/ankan/.mozilla/firefox/o2walj7p.whatsapp/'
    path_to_driver = '/home/ankan/Projects/pyzapp/selenium/webdriver/geckodriver/geckodriver'

    pywhatsapp = PyWhatsApp(path_to_profile, path_to_driver)
    pywhatsapp.sendMessage("\"" + args.friend + "\"", args.message)


if __name__ == "__main__":
    main()
