from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

nav = Firefox()
nav.get(url)
sleep(5)
ancora = nav.find_element(By.TAG_NAME, 'a')
##nesse caso, o codigo só vai pegar a tag html inicial
# numero =  nav.find_element(By.TAG_NAME, 'p')
###nesse caso, o codigo vai pegar todas as tags
# numero =  nav.find_elements(By.TAG_NAME, 'p')


for clicks in range (10):
    nums = nav.find_elements(By.TAG_NAME, 'p')
    ancora.click()
    print(f'valor do ulti paragrafo: {nums[-1].text} valor do click: {clicks}')
    ##dessa forma da false pois o num do html é string
    print(f'Os valores são iguais {nums[-1].text == str(clicks)}')

# print(numero.text)

# ancora.click()
# ancora.click()
