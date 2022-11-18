import requests
from bs4 import BeautifulSoup
#from lxml import etree

def consultar(pagina):
    headers = {'user-agent': 'Mozilla/5.0'}

    url = pagina
    site = requests.get(url=url, timeout=15, headers=headers)
    siteText = site.text
    sitePolido = BeautifulSoup(siteText,"html.parser")

    sitePolido = sitePolido.find_all("section",{"id":"content"})[0]

    produtosNome=sitePolido.find_all("b",{"class":"product-name"})
    produtosPreco=sitePolido.find_all("span", {"class":"best-price"})
    produtosLink =sitePolido.find_all("span", "box-item")

    contador=0
    nome = []
    preco = []
    foto = []
    while contador < len(produtosNome):
        #print(produtosNome[contador].text)
        #print(produtosPreco[contador].text)
        #print(produtosLink[contador]['href'])
        nome.append(produtosNome[contador].text)
        preco.append(produtosPreco[contador].text)
        foto.append(produtosLink[contador].find_all("img")[0]['src'])
        #print(len(foto))
        #print(contador)
        #print("")
        contador += 1
    return [nome, preco, foto]
    #print(len(produtosNome))
#print(consultar()[0])
#print(consultar()[2])
#print(len(consultar()[2]))
