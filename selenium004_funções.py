from selenium.webdriver import Firefox
from time import sleep 
from selenium.webdriver.common.by import By

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

sleep(1)
def find_by_a(browser,tag, my_tag):
    elemento = browser.find_elements(By.TAG_NAME, tag)
    for i in elemento:
        if my_tag in i.text:
            return i.text
        
# finded = find_by_a(browser, 'a', 'Goog')
# print(finded, finded.get_attribute('href'))

def search_by_href(browser, my_atributte):
    elemento = browser.find_elements(By.TAG_NAME, 'a')
    for i in elemento:
        if my_atributte in i.get_attribute('href'):
            return i
find = search_by_href(browser, 'goo')
print(find.get_attribute('href'))



# first_ul = browser.find_element(By.TAG_NAME,'ul')
# first_li = first_ul.find_elements(By.TAG_NAME, 'li')
# first_a = first_li[1].find_element(By.TAG_NAME, 'a')

# print(first_a.text)



