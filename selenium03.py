from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()

browser.get(url)
sleep(1)

element_a = browser.find_element(By.TAG_NAME,'a')
element_p = browser.find_elements(By.TAG_NAME,'p')
num_esperado = element_p[-1].text[-1]
# element_p = browser.find_elements(By.TAG_NAME,'p')
# num_esperado = element_p[-1].text[-1]
# print(num_esperado)
for i in range(100):
    element_a.click()
    atual = browser.find_elements(By.TAG_NAME,'p')
    num_atual = atual[-1].text[-1]
    if num_atual == num_esperado:
        print(f'num esperado:{num_esperado} num atual:{num_atual}')
        break
