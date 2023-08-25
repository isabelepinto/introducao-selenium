from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

driver.get(url)
sleep(2)

a = driver.find_element(By.LINK_TEXT, 'clique aqui')
    
while True:  
    a.click()
    sleep(0.200)
    elements_p = driver.find_elements(By.TAG_NAME, 'p')  
    textos = []
    ganhou = False
    for t in elements_p:
        textos.append(t.text)
        if 'ganhou' in t.text:
            ganhou = True
            break
    if ganhou:
        break        

driver.quit()
