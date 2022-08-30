#coding:utf-8
import json
import pickle
import pyautogui
import time
from keywords import key_words_search
from pathlib import Path
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains



class Userbot:

	def __init__(self, login, password):
		self.login       = login 
		self.password    = password
		self.path_driver = "/home/anoleose/Downloads/geckodriver"
		self.driver      = webdriver.Firefox(executable_path=self.path_driver)
		self.maxwind     = self.driver.maximize_window()
		self.websites    = ["https://www.yandex.ru"]


	def load_cookie(self):
		try:
			login = self.login
			config = Path(f"my_cookies/{login}-cookies.json")
			cookies = json.load(open(config, "r"))
			print("connecting...")
			for website in self.websites:
				self.driver.get(website)
				time.sleep(randrange(10, 30))
				for cookie in cookies:
					self.driver.add_cookie(cookie)
				self.driver.refresh()
		except Exception as e:
			print("create new cookie")
			for website in self.websites:
				self.driver.get(website)
				time.sleep(randrange(10, 30))
		

	def signup(self):
		print("navigating...")
		button = self.driver.find_element(By.CLASS_NAME, "desk-notif-card__login-new-item-title")
		button.click()
		time.sleep(randrange(5, 10))

		enter_email = self.driver.find_element(By.ID, "passp-field-login")
		enter_email.send_keys(self.login, Keys.ENTER)
		time.sleep(randrange(5, 10))

		enter_password = self.driver.find_element(By.ID, "passp-field-passwd")
		enter_password.send_keys(self.password, Keys.ENTER)
		time.sleep(randrange(5, 10))
		

	def search_random_word(self):
		key_words = key_words_search()
		s_random = randrange(0, 6)
		word = key_words[s_random]
		search_button = self.driver.find_element(By.ID, "text")
		search_button.send_keys(word, Keys.ENTER)
		

	def save_cookie(self):
		print("save cookie...")
		login = self.login
		with open(f"my_cookies/{login}-cookies.json","w") as file:
			json.dump(self.driver.get_cookies(), file) 


	def main_process(self):
		self.load_cookie()
		try:
			self.signup()
			self.save_cookie()
		except Exception as e:
			pass
		self.search_random_word()
		time.sleep(randrange(60, 120))



if __name__ == "__main__":
	while(True):
		u = Userbot("login", "password")
		u.main_process()
		time.sleep(randrange(30, 60))












