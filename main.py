from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os


class GmailUserNameChecker:

    def __init__(self, headless=False, driver='chromium'):
        if driver == 'chromium':
            options = Options()
            if headless == True:
                options.add_argument('--headless')

            options.add_argument('--disable-gpu')
            options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
            driver = webdriver.Chrome(
                os.environ['DRIVER_PATH'], chrome_options=options)
            url = 'https://accounts.google.com/signup/v2/webcreateaccount'
            browser = driver.get(url)
        elif driver == 'firefox':
            pass

    def check_username(self):
        for x in range(1000):
            input1 = self.browser.find_element_by_id('username')
            input1.send_keys(os.environ['KEYWORD']+str(x))
            input2 = input1.send_keys(Keys.TAB)
            time.sleep(2)
            error = self.browser.find_element_by_class_name("LXRPh").text
            print(error)
            time.sleep(2)
            input1.clear()
            self.browser.quit()


if __name__ == '__main__':
    gmail = GmailUserNameChecker()
    gmail.check_username()
