from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

#Extrair todos os títulos
nome_produto = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
#Extrair preço do produto
preco_produto = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")
#Criando a planilha
workbook = openpyxl.Workbook()
#Criando a página produtos
workbook.create_sheet('produtos site')
#Selecionando a página produtos
pagina_planilha = workbook['produtos site']
#Classificando a primeira coluna como 'Produto'
pagina_planilha['A1'].value = 'Produto'
#Classificando a segunda coluna como 'Valor' 
pagina_planilha['B1'].value = 'Valor'

for nome, valores in zip(nome_produto, preco_produto):
    pagina_planilha.append([nome.text, valores.text])


workbook.save('produtos-site.xlsx')        