from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

driver.get(url)
sleep(2)

element = driver.find_element(By.TAG_NAME, 'h1')
h1 = element.text

elements_p = driver.find_elements(By.TAG_NAME, 'p')

textos = []
atributos = []
for t in elements_p:
    pegar_atributos = t.get_attribute('atributo')
    atributos.append(pegar_atributos)
    textos.append(t.text)

#print('atributos=',atributos)
#print('textos=',textos)

dicionario = {h1:
            {atributos[0]: textos[0],
             atributos[1]: textos[1],
             atributos[2]:textos[2]            
             }}

print(dicionario)

driver.close()
