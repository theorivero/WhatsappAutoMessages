from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class ContactRow:
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone


def humanize_text(textfield, message):
	words = message.split(' ', maxsplit=10)
	for word in words:
		textfield.send_keys(word)
		textfield.send_keys(' ')
		sleep(0.3)
	textfield.send_keys("\n")

class WhatsBot:
	def __init__(self):
		self.webdriver = Firefox()
		self.url = 'https://web.whatsapp.com/'

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
				humanize_text(txt_box, message)

		except:
			print('erro')

		
		
	def close(self):
		sleep(10)
		self.webdriver.close()
		self.webdriver.quit()