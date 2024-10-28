from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://game-numero-secreto-plum.vercel.app/'

nav = Firefox()
nav.get(url)
sleep(3)
txt_num_secreto = nav.find_element(By.TAG_NAME, 'p')
campo = nav.find_element(By.TAG_NAME,'input')

nav.campo.get(numero)
print(type(txt_num_secreto))
print(type(campo))

print(txt_num_secreto.text)
print(campo.text)