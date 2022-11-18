import requests
from bs4 import BeautifulSoup
#from lxml import etree

headers = {'user-agent': 'Mozilla/5.0'}

url = "https://www.portaldascameras.com/alarme-e-cerca"
site = requests.get(url=url, timeout=15, cookies=True)
siteText = site.text
sitePolido = BeautifulSoup(siteText,"html.parser")


#print(sitePolido)
#sitePolido = sitePolido.xpath(id)
sitePolido = sitePolido.find_all("section",{"id":"content"})[0]

#print(sitePolido)
#ResultItems_33443112

produtosNome=sitePolido.find_all("b",{"class":"product-name"})
produtosPreco=sitePolido.find_all("span", {"class":"best-price"})
produtosLink =sitePolido.find_all("a", "product-image")

#.contents filhos
#print(produtosPreco)

contador=0
while contador < len(produtosNome):
    print(produtosNome[contador].text)
    print(produtosPreco[contador].text)
    print(produtosLink[contador]['href'])
    foto = produtosLink[contador].find_all("img")[0]['src']
    print(foto)
    print(contador)
    print("")
    contador += 1

print(len(produtosNome))
    
#print(produtosNome[0].text)
#print(produtosNome[1].text)


