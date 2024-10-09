#Passo 1: entrar no sistrma https://dlp.hashtagtreinamentos.com/python/intensivao/login

import time
import pyautogui

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#PAsso 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=801, y=543)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha aqui")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

#passo 3: importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#passso 4: cadastrar 1 produto


linha = 0
for linha in tabela.index:

    pyautogui.click(x=652, y=393)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")  

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)


#passo 5 : repetir o processo de cadastro até acabar os produtos

