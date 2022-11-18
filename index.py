from flask import Flask, render_template
import scraping
import dados
#print(os.path())


app = Flask(__name__)

class listaProdutos():
    produtos = []
    precos = []
    imagens = []
    itensSeguranca = scraping.consultar("https://www.portaldascameras.com/seguranca")
    itensAlarmeECercas = scraping.consultar("https://www.portaldascameras.com/alarme-e-cerca")
    itensControleDeAcesso = scraping.consultar("https://www.portaldascameras.com/controle-de-acesso")
    itensTelefoniaEInterfonia = scraping.consultar("https://www.portaldascameras.com/telefonia-e-interfonia")
    itensEletronicos = scraping.consultar("https://www.portaldascameras.com/eletronicos")
    itenInformatica = scraping.consultar("https://www.portaldascameras.com/informatica")
    unidos = [
        itensSeguranca,
        itensAlarmeECercas,
        itensControleDeAcesso,
        itensTelefoniaEInterfonia,
        itensEletronicos,
        itenInformatica
    ]
    for unidade in unidos:
        contador = 0
        porcentagem = 20
        while (contador < len(unidade[0])):
            produtos.append(unidade[0][contador])
            #print(unidade[1][contador])
            preco=unidade[1][contador].replace('por R$ ','')
            preco=preco.replace('  á vista','')
            #print(preco)
            preco=preco.replace('.','')
            preco=preco.replace(',','.')
            preco=float(preco)
            preco = (preco*(100+porcentagem)/100)
            preco=str(f'{preco:.2f}')
            preco = 'R$ '+preco.replace('.',',')
            #print(preco)
            #precos.append(unidade[1][contador])
            precos.append(preco)
            imagens.append(unidade[2][contador])
            contador+=1
                
                

def gerarProdutos(itens, valores, fotos):
    produtosHTML = ""
    contador = 0
    while (contador < len(itens)):
        if contador % 4 == 0:
            produtosHTML += f'\n		<div class="produtos">'
        if contador % 2 == 0:
            produtosHTML += f'\n			<div class="produtosDupla">'
        
        foto = fotos[contador].replace(
            fotos[contador][fotos[contador].find('-')+1:fotos[contador].find('-')+8],
            "500-500")
        
        msg = f"https://api.whatsapp.com/send?phone=5511989182294&text=Olá, desejo adquirir o produto *{itens[contador]}* que encontrei em seu site"
        msg = msg.replace(" ","%20")
        
        produtosHTML += f"""
                <a href="{msg}" target="_blank">
                    <div class="produto">
                        <div class="produtoFoto">
                            <img src="{foto}">
                        </div>
                        <div class="produtoNome">
                            <h3>{itens[contador]}</h3>
                        </div>
                        <div class="produtoPreco">
                            <p>{valores[contador]}</p>
                        </div>
                    </div>
                </a>"""
        contador += 1
        if contador % 2 == 0:
            produtosHTML += f'\n			</div>'
        if contador % 4 == 0:
            produtosHTML += f'\n		</div>'
    return produtosHTML

@app.route("/")
def homepage():
    filtros = [
        "seguranca",
        "alarme-e-cerca",
        "controle-de-acesso",
        "telefonia-e-interfonia",
        "eletronicos",
        "informatica"]
    produtos = gerarProdutos(
        itens=listaProdutos.produtos,
        valores=listaProdutos.precos,
        fotos=listaProdutos.imagens)
    return render_template("inicio.html", produtos=produtos, filtros=filtros)

@app.route("/filtro/<filtrado>")
def filtrado(filtrado):
    filtros = [
        "seguranca",
        "alarme-e-cerca",
        "controle-de-acesso",
        "telefonia-e-interfonia",
        "eletronicos",
        "informatica"]
    tudo = dados.itensTabela(filtro=filtrado, pasta="https://venicio.herokuapp.com")
    produtos = gerarProdutos(
        itens=tudo[0],
        valores=tudo[1],
        fotos=tudo[2])
    return render_template("inicio.html", produtos=produtos, filtros=filtros)

if __name__ == "__main__":
    app.run(debug=True)