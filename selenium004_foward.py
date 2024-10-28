from selenium.webdriver import Firefox
from time import sleep 
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

def find_by_a(browser,tag, my_element):
    elemento = browser.find_elements(By.TAG_NAME, tag)
    for i in elemento:
        if i.text == my_element:
            return i
        
browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')
sleep(1)

botoes = ['um','dois','tres','quatro']
for botao in botoes:
    find_by_a(browser, 'div', botao).click()
    sleep(0.3)

for i in botoes:
    browser.back()
    sleep(0.5)
for i in botoes:
    browser.forward()
    sleep(0.5)
print(browser.current_url)
print(urlparse(browser.current_url))

# botao = find_by_a(browser, 'div', 'um').click()
