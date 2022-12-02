from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://127.0.0.1:5500/app/index.html')

about_element = driver.find_element("id", "about")
time.sleep(2)
about_element.click()
time.sleep(2)
print('--------------- TELA SOBRE EXECUTADA ---------------')
