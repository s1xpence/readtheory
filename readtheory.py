# reddit.py
from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotVisibleException


options = webdriver.ChromeOptions()

# replace binary path with your own below

options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

options.add_argument('window-size=800x841')

# uncomment line 19 if you want chrome to run without window
# in background

# options.add_argument('headless') 

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://readtheory.org/auth/login')

# change username and password to match your own. this is a
# throwaway password i've implemented, so don't get any funny
# ideas :)

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('14367@students.isb.ac.th')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('mhNF2PqdfjF3W')

login_click = driver.find_element_by_xpath('//*[@id="ajaxLogin"]').click()

x = 1
while x == 1:
	try:

		# this is to select one of the answers
		answer_click = driver.find_element_by_xpath('//*[@class="answer-label"]').click()

		# this is to click the 'submit answer' button
		submit_click = driver.find_element_by_xpath('//*[@id="presentQuizForm-answerQuestionButton"]').click()

		time.sleep(5)

		next_button = driver.find_element_by_xpath('//input[@id="presentQuizForm-nextQuestionButton"]').click()

		driver.refresh()

	except ElementNotVisibleException:
		driver.refresh()
 
#https://medium.com/@stevennatera/web-scraping-with-selenium-and-chrome-canary-on-macos-fc2eff723f9e




