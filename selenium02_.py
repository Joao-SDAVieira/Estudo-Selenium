from selenium.webdriver import Firefox
from time import sleep 
from selenium.webdriver.common.by import By
browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

unorder_list = browser.find_element(By.TAG_NAME, 'ul')

list_item = unorder_list.find_elements(By.TAG_NAME, 'li')

list_item = list_item[0].text

print(list_item)