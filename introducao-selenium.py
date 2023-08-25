from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # inicializa o browser 

url = 'https://curso-python-selenium.netlify.app/aula_03.html' # salvando a url do site
driver.get(url) # entrando o site
driver.fullscreen_window()

sleep(1)

link = driver.find_element(By.LINK_TEXT, "minha ancora") # busca o texto do link
link.click() # clica no link encontrado
link.click() # clica no link encontrado
link.click() # clica no link encontrado

# p = driver.find_element(By.TAG_NAME, "p")
# print(p.text)


# elementos = driver.find_elements(By.TAG_NAME, 'a')

# for e in elementos:
#     print(e.text)

#driver.quit() # fecha o browser
