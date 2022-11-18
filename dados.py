arquivo = __file__
arquivoInvertido = arquivo[::-1]
arquivoTamanho = len(arquivo)
caminho = arquivo[0:arquivoTamanho-arquivoInvertido.find("\\")]

def itensTabela(filtro):
    with open(caminho+rf'\static\dados\{filtro}.csv', 'r', encoding="utf_8") as file:
        dados = file.read()
        linhas = dados.split("\n")
        #qtdColunas = len(linhas[0].split("ç;ç"))
        dados = [[],[],[]]
        contador = 1
        while (contador < len(linhas)-1):
            celulas = linhas[contador].split("ç;ç")
            dados[0].append(celulas[0])
            dados[1].append(celulas[1])
            dados[2].append(celulas[2])
            contador+=1
        #print(dados[2])
    return dados
        
itensTabela("alarme-e-cerca")