from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://127.0.0.1:5500/app/index.html')