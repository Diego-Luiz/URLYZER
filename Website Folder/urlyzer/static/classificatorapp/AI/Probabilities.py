import os
def read():
    pasta = os.path.dirname(os.path.abspath(__file__))
    nome_arquivo = os.path.join(pasta, "Probabilidades.txt")
    arquivo = open(nome_arquivo,"r",encoding='Latin1')
    linhas = arquivo.readlines()
    lista = []
    dictio = {}
    for i in linhas:
        lista = i.split(',')
    for i in lista:
        if len(i.split('^')) == 2:
            dictio[i.split('^')[0]] = float(i.split('^')[1])
    arquivo.close()
    return dictio
    
#p/gravar Dictionary
def write(Dictionary):
    arquivo = open('Modules/Probabilidades.txt',"w",encoding='Latin1')
    for i,j in Dictionary.items():
        arquivo.write(i+'^'+str(j)+',')
    arquivo.close()
    print('Arquivo Probabilidades.txt salvo!')
