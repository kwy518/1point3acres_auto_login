from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), 
	chrome_options=chrome_options)

SLEEP_TIME = 4

# Activate chrome to access website
driver.get('http://www.1point3acres.com/bbs/')
print('Successful Access Site')

# Login
driver.find_element_by_id("ls_username").send_keys(os.environ.get("USERNAME"))
driver.find_element_by_id("ls_password").send_keys(os.environ.get("PASSWORD"))
time.sleep(SLEEP_TIME)
driver.find_element_by_css_selector("button.pn.vm").click()
print('Successful Login')
time.sleep(SLEEP_TIME)

# Click Daily Reward
driver.find_element_by_xpath("//font[text()='签到领奖!']").click()
time.sleep(SLEEP_TIME)
print('Successful click Daily Reward')

# Choose Mood
driver.find_element_by_css_selector("#kx > center > img").click()
time.sleep(SLEEP_TIME)
print('Successful Choose Mood')

# Quick select
driver.find_element_by_xpath("(//input[@name='qdmode'])[2]").click()
print('Successful Autofill review')
time.sleep(SLEEP_TIME)

# Submit
# driver.find_element_by_css_selector("button.pn.pnc").click()
# print('Successful Submit daily request')

# Quit
driver.quit()
exit(0)
