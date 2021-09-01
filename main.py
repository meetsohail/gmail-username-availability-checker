from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument(
    "user-agent=[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36]")

driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)
url = 'https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
driver.get(url)
for x in range(1000):
    input1 = driver.find_element_by_id('username')
    input1.send_keys("sohail"+str(x))
    input2 = input1.send_keys(Keys.TAB)
    time.sleep(2)
    error = driver.find_element_by_class_name("LXRPh").text
    print(error)
    time.sleep(2)
    input1.clear()
    driver.quit()
