import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Changed this variable with the path of the profile
path_to_profile = '/Users/hercules/Library/Application Support/Firefox/Profiles/iqi1xm8d.default'

# Name of your friend and the message you want to send, comes from command line
friend = sys.argv[1]   # 'Tanmoy'
message = sys.argv[2]  # "Banchod leura saala"
print(friend, message)

# Creates a FirefoxProfile object with the path of the profile you gave
profile = webdriver.FirefoxProfile(path_to_profile)
# Opens the automated Firefox browser using the profile object
browser = webdriver.Firefox(profile)
# Opens whatsapp web
browser.get("https://web.whatsapp.com/")
# Creates a Wait object which specifies how long you'll wait to locate the presence of any element.
# We are waiting for 600 milliseconds
wait = WebDriverWait(browser, 600)

# xpath for the span whose title attribute is the friend's name
x_arg = '//span[@title="{}"]'.format(friend)
# Wait until the presence of the element having the above xpath is located and select it
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
# Click on the selected element i.e., the chat with the friend, so that it is selected
group_title.click()

# Put this block in a loop, if you are evil

# xpath for the div whose class attribute contains "copyable-text selectable-text"
inp_xpath = '//div[contains(@class, "copyable-text selectable-text")]'
# Wait until the presence of the element having the above xpath is located and select it
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
# Type the message in and press Enter key
input_box.send_keys(message + Keys.ENTER)

# Wait for 5 seconds so that the message is sent and then close the browser
time.sleep(5)
browser.close()
