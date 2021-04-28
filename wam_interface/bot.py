from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import os

class ContactRow:
	def __init__(self, name, phone, company, att1, att2):
		self.name = name
		self.phone = phone
		self.company = company
		self.att1 = att1
		self.att2 = att2

def humanize_text(textfield, message, contact):
	words = message.split(' ', maxsplit=10)
	for word in words:
		if "{nome}" in word:
			word = word.replace("{nome}", contact.name)
		if "{empresa}" in word:
			word = word.replace("{empresa}", contact.company)
		if "{att1}" in word:
			word = word.replace("{att1}", contact.att1)
		if "{att2}" in word:
			word = word.replace("{att2}", contact.att2)

		textfield.send_keys(word)
		textfield.send_keys(' ')
		sleep(0.3)
	textfield.send_keys("\n")

class WhatsBot:
	def __init__(self):
		self.webdriver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=get_chrome_options())
		self.url = 'https://web.whatsapp.com/'

	def get_chrome_options(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
		return chrome_options


	def open(self):
		self.webdriver.get(self.url)
		self.webdriver.maximize_window()

	def login(self):
		login_wait = WebDriverWait(self.webdriver, 60) 
		login_check_locator = (By.CSS_SELECTOR, 'span div._2n-zq div span')
		login_wait.until(
			presence_of_element_located(login_check_locator),
			"Não fez login"
			)
		print('login feito')

	def send_message(self, contact, messages):
		message_wait = WebDriverWait(self.webdriver, 30) 

		self.webdriver.get(f'https://web.whatsapp.com/send?phone=55{contact.phone}&source=&data=#')

		txt_box_locator = (By.CSS_SELECTOR , 'div._2A8P4 div._1JAUF._2x4bz div._2_1wd.copyable-text.selectable-text')
		
		try:
			message_wait.until(
				presence_of_element_located(txt_box_locator),
				"Não achou o textbox"
				)
		
			txt_box = self.webdriver.find_element(*txt_box_locator)
		
			for message in messages:
				humanize_text(txt_box, message, contact)

		except Exception as e:
			print(e)

		
	def close(self):
		sleep(10)
		self.webdriver.close()
		self.webdriver.quit()
