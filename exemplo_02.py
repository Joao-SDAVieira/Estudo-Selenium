
from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By

from time import sleep



url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'



boas_vindas = {}

browser = Firefox()

browser.get(url)

sleep(3)

chave1 = browser.find_elements(By.CLASS_NAME, 
'atributo')



print(chave1[-1])

# for texto in range(7):

# chave1 = browser.find_elements(By.CLASS_NAME, 'atributo')

# print(chave1[-1].text)









# lista_dic.append(chave)
# print(lista_dic)

# lista_dic[0] = dict()

# print(lista_dic)
