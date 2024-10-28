from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
navegador = Firefox()
navegador.get(url)
sleep(3)

botao = navegador.find_element(By.TAG_NAME, 'a')

# def verificar_ganhou(valor_num_esperado, valor_num_atual):
#     if valor_num_esperado == valor_num_atual:
#             return True
#     else:
#           return False


num_esperado = navegador.find_elements(By.TAG_NAME, 'p')
num_esperado = num_esperado[-1].text
num_esperado = num_esperado[-1]

print(num_esperado)

for i in range(2,101):
    botao.click()
    num_atual = navegador.find_elements(By.TAG_NAME, 'p')
    # print(num_atual[i].text)
    # if i == 1:
    #     num_atual = num_atual[2].text
    # else:
    #     num_atual = num_atual[i].text
    num_atual= num_atual[i].text
    # comparacao = verificar_ganhou(num_atual[-1],num_esperado)
    if num_atual[-1] == num_esperado:
        print('acertou')
        break
    

# for i in range(1,101):
#     botao.click()
#     num_atual = navegador.find_elements(By.TAG_NAME, 'p')
#     # print(num_atual[i].text)
#     if i == 1:
#         num_atual = num_atual[2].text
#     else:
#         num_atual = num_atual[i].text
    
#     # comparacao = verificar_ganhou(num_atual[-1],num_esperado)
        
#     if num_atual[-1] == num_esperado:
#         print('acertou')
#         break



sleep(10)

navegador.quit()