from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(4)

titulo = browser.find_element(By.TAG_NAME,'h1')
print(titulo.text)
dicio = {titulo.text: 'Vazio'}
dicio2 = {}
for numero in range(3):
    paragrafo = browser.find_elements(By.TAG_NAME,'p')
    print(paragrafo[numero].text)

    dicio2.update({f'texto{numero + 1}': paragrafo[numero].text})


#print(dicio2)
dicio = {titulo.text: dicio2}
print(dicio)