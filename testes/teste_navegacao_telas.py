from selenium import webdriver
import pyscreenshot as ImageGrab
from datetime import datetime
import os
import time


## abrir a página
driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('http://127.0.0.1:5500/app/index.html')

#CRIAR UM DIRETORIO COM A DATA ATUAL
data = datetime.now()
dt_string = data.strftime("%Y%m%d_%H%M%S")
diretorio = "testes/evidencias/" + dt_string
os.mkdir(diretorio)

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_1.png") 

## entrar no menu "Sobre"
time.sleep(1)
about_element = driver.find_element("id", "about")
about_element.click()
time.sleep(1)
print('--------------- TELA SOBRE EXECUTADA ---------------')

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_2.png") 

## entrar no menu "Produtos"
time.sleep(1)
products_element = driver.find_element("id", "products")
products_element.click()
time.sleep(1)
print('--------------- TELA PRODUTOS EXECUTADA ---------------')

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_3.png") 

## entrar no menu "Venda Conosco"
time.sleep(1)
products_element = driver.find_element("id", "sell")
products_element.click()
time.sleep(1)
print('--------------- TELA VENDA CONOSCO EXECUTADA ---------------')

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_4.png") 

## entrar no menu "Contato"
time.sleep(1)
products_element = driver.find_element("id", "contato")
products_element.click()
time.sleep(1)
print('--------------- TELA CONTATO EXECUTADA ---------------')

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_5.png") 

## entrar no menu "Index"
time.sleep(1)
products_element = driver.find_element("id", "index")
products_element.click()
time.sleep(1)
print('--------------- TELA HOME EXECUTADA ---------------')

#TIRAR PRINT
image = ImageGrab.grab()

#SALVAR A EVIDENCIA NO DIRETORIO
image.save(diretorio + "/evidencia_6.png") 

driver.close()