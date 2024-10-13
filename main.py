# Cadastro Automatico

#Primeiro Passo: Importar bibliotecas
import pyautogui
from time import sleep
import pandas

pyautogui.PAUSE = 0.5

#Segundo Passo: Abrir o navegador

#Abrir pesquisa do windows
pyautogui.press('win')
#Pesquisar Navegador
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(1)

#Terceiro Passo: Acessar o site
#Selecionar Perfildo chrome
pyautogui.click(x=1292, y=434)
sleep(1)
#Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
sleep(2)

#Quarto Passo: Fazer o login
#Clicar no campo de cadastro
pyautogui.click(x=856, y=427)
#Escrever E-mail
pyautogui.write("fernandoteste@email.com")
#Ir para o próximo campo
pyautogui.press('tab')
#Escrever Senha
pyautogui.write("41546544438")
#Clicar em Entrar
pyautogui.press('tab')
pyautogui.press('enter')

#Quinto Passo: Abrir o Banco de Dados

tabela = pandas.read_csv("produtos.csv")

#Sexto Passo: Cadastrar Produtos

for linha in tabela.index:
    #seleciona campo
    pyautogui.click(x=714, y=316)
    #pega o valor específico da tabela que preenche o campo
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo
    pyautogui.write(str(codigo))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    marca = tabela.loc[linha, "marca"]
    #preencher o campo
    pyautogui.write(str(marca))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    tipo = tabela.loc[linha, "tipo"]
    #preencher o campo
    pyautogui.write(str(tipo))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    categoria = tabela.loc[linha, "categoria"]
    #preencher o campo
    pyautogui.write(str(categoria))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    preco = tabela.loc[linha, "preco_unitario"]
    #preencher o campo
    pyautogui.write(str(preco))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    custo = tabela.loc[linha, "custo"]
    #preencher o campo
    pyautogui.write(str(custo))
    #pular para o proximo campo
    pyautogui.press('tab')
    
    #preencher o campo de observação se ouver informação caso contrario o campo será pulado
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    #rolar a página para cima
    pyautogui.scroll(500)