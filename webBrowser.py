from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path=r'/home/mabo/Work/KendryAlert/geckodriver') # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
assert "Yahoo!" in browser.title
elem = browser.find_element_by_name("p") # Find the query box

browser.close()