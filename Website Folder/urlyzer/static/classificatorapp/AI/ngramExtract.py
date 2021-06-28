from urllib.parse import urlparse
import os
import csv
import nltk
# Modulo para ler/escrever o dicionario de probabilidades em arquivo de texto
from . import Probabilities
#import Probabilities
'''
Função para criar o dicionário de probabilidades, relação 'chave':probabilidade de acordo com o dataset benigno
'''
def getProbabilities(Arq):
    Probabilidades = {}
    final = []
    with open(Arq, 'r', encoding='Latin1') as benigns:
        csv_reader = csv.reader(benigns)
        csv_reader.__next__()  # p/nao ler o indice
        for url_list in csv_reader:
            # pegando a URL corresponde à aquela posição
            url_string = url_list[0]
            if url_string[0:2] == '//':
                url_string = url_string[2:]
            for i in range(1, 5):  # unigram,bigram,trigram, fourgram
                ngram = nltk.ngrams(url_string, i)
                final.extend(list(map(''.join, ngram)))

    for j in final:
        Probabilidades[j] = 0
    freqs = nltk.FreqDist(final)

    # Frequencias de todos os unigrams
    uni = [v for k, v in freqs.items() if len(k) == 1]
    SumUni = sum(uni)  # Soma da frequencia de todos os unigrams

    # Calcular as probabilidades
    for key in Probabilidades.keys():
        if len(key) == 1:  # se for unigram
            Probabilidades[key] = freqs[key] / SumUni
        else:  # se for bigram,trigram,fourgram
            Probabilidades[key] = freqs[key] / freqs[key[:len(key)-1]]
    Probabilities.write(Probabilidades)

def readProbabilities():
    return Probabilities.read()
'''
Função para extrair as características de N-Gramas referente a uma URL
'''
def extractFeatures(Url,Probabilidades):
    url_parse = urlparse(Url)
    url_string = Url
    if url_string[0:2] == '//':
        url_string = url_string[2:]

    SimFields = {
        'URLUnigram': 0, 'URLBigram': 0, 'URLTrigram': 0, 'URLFourgram': 0,
        'HostUnigram': 0, 'HostBigram': 0, 'HostTrigram': 0, 'HostFourgram': 0,
        'PathUnigram': 0, 'PathBigram': 0, 'PathTrigram': 0, 'PathFourgram': 0,
        'T_MT_U': 0, 'T_MT_DOM': 0, 'T_MT_CM': 0, 'T_MT_P': 0, 'Q_T_U': 0
    }
    
    #============================== Características de Tokens URL
    lista1 = nltk.tokenize.regexp_tokenize(url_string,"[\w']+")
    lista2 = nltk.tokenize.regexp_tokenize(url_string,"[\W']+")
    lista3 = {x:len(x) for x in lista1}
    lista4 = {x:len(x) for x in lista2}
    for i in lista4.items():
        lista3[i[0]] = i[1]
    #LISTA3 CONTEM TODOS OS TOKENS DAQUELA PARTE
    SimFields['Q_T_U'] = len(lista3)
    SimFields['T_MT_U'] = max(lista3.values())
    #================================
    # ===========================> URL Url
    unigramList = list(map(''.join, nltk.ngrams(url_string, 1)))
    bigramList = list(map(''.join, nltk.ngrams(url_string, 2)))
    trigramList = list(map(''.join, nltk.ngrams(url_string, 3)))
    fourgramList = list(map(''.join, nltk.ngrams(url_string, 4)))
    # Dicionários
    unigramDict = {x: 0 for x in unigramList}
    bigramDict = {x: 0 for x in bigramList}
    trigramDict = {x: 0 for x in trigramList}
    fourgramDict = {x: 0 for x in fourgramList}

    # Similaridade unigram
    if len(unigramDict) > 0:
        for i in unigramDict.keys():
            if i in Probabilidades:
                SimFields['URLUnigram'] = SimFields['URLUnigram'] + Probabilidades[i]
        SimFields['URLUnigram'] = SimFields['URLUnigram'] / len(unigramDict)
    # Similaridade biggram
    if len(bigramDict) > 0:
        for i in bigramDict.keys():
            if i in Probabilidades:
                SimFields['URLBigram'] = SimFields['URLBigram'] + Probabilidades[i]
        SimFields['URLBigram'] = SimFields['URLBigram'] / len(bigramDict)
    # Similaridade trigram
    if len(trigramDict) > 0:
        for i in trigramDict.keys():
            if i in Probabilidades:
                SimFields['URLTrigram'] = SimFields['URLTrigram'] + Probabilidades[i]
        SimFields['URLTrigram'] = SimFields['URLTrigram'] / len(trigramDict)
    # Similaridade fourgram
    if len(fourgramDict) > 0:
        for i in fourgramDict.keys():
            if i in Probabilidades:
                SimFields['URLFourgram'] = SimFields['URLFourgram'] + Probabilidades[i]
        SimFields['URLFourgram'] = SimFields['URLFourgram'] / len(fourgramDict)

    # ==========================> Host (netloc)
    #============================== Características de Tokens Dominio
    lista1 = nltk.tokenize.regexp_tokenize(url_parse.netloc,"[\w']+")
    lista2 = nltk.tokenize.regexp_tokenize(url_parse.netloc,"[\W']+")
    lista3 = {x:len(x) for x in lista1}
    lista4 = {x:len(x) for x in lista2}
    for i in lista4.items():
        lista3[i[0]] = i[1]
    #LISTA3 CONTEM TODOS OS TOKENS DAQUELA PARTE
    if len(lista3) > 0:
        SimFields['T_MT_DOM'] = max(lista3.values())        
    #================================
    unigramList = list(map(''.join, nltk.ngrams(url_parse.netloc, 1)))
    bigramList = list(map(''.join, nltk.ngrams(url_parse.netloc, 2)))
    trigramList = list(map(''.join, nltk.ngrams(url_parse.netloc, 3)))
    fourgramList = list(map(''.join, nltk.ngrams(url_parse.netloc, 4)))
    # Dicionários
    unigramDict = {x: 0 for x in unigramList}
    bigramDict = {x: 0 for x in bigramList}
    trigramDict = {x: 0 for x in trigramList}
    fourgramDict = {x: 0 for x in fourgramList}

    # Similaridade unigram
    if len(unigramDict) > 0:
        for i in unigramDict.keys():
            if i in Probabilidades:
                SimFields['HostUnigram'] = SimFields['HostUnigram'] + Probabilidades[i]
        SimFields['HostUnigram'] = SimFields['HostUnigram'] / len(unigramDict)
    # Similaridade biggram
    if len(bigramDict) > 0:
        for i in bigramDict.keys():
            if i in Probabilidades:
                SimFields['HostBigram'] = SimFields['HostBigram'] + Probabilidades[i]
        SimFields['HostBigram'] = SimFields['HostBigram'] / len(bigramDict)
    # Similaridade trigram
    if len(trigramDict) > 0:
        for i in trigramDict.keys():
            if i in Probabilidades:
                SimFields['HostTrigram'] = SimFields['HostTrigram'] + Probabilidades[i]
        SimFields['HostTrigram'] = SimFields['HostTrigram'] / len(trigramDict)
    # Similaridade fourgram
    if len(fourgramDict) > 0:
        for i in fourgramDict.keys():
            if i in Probabilidades:
                SimFields['HostFourgram'] = SimFields['HostFourgram'] + Probabilidades[i]
        SimFields['HostFourgram'] = SimFields['HostFourgram'] / len(fourgramDict)

    # ==========================> Path (path)
    if url_parse.path and url_parse.path!='/':
        #============================== Características de Tokens Caminho
        lista1 = nltk.tokenize.regexp_tokenize(url_parse.path,"[\w']+")
        lista2 = nltk.tokenize.regexp_tokenize(url_parse.path,"[\W']+")
        lista3 = {x:len(x) for x in lista1}
        lista4 = {x:len(x) for x in lista2}
        for i in lista4.items():
            lista3[i[0]] = i[1]
        #LISTA3 CONTEM TODOS OS TOKENS DAQUELA PARTE
        if len(lista3) > 0:
            SimFields['T_MT_CM'] = max(lista3.values())
        #================================
        unigramList = list(map(''.join, nltk.ngrams(url_parse.path, 1)))
        bigramList = list(map(''.join, nltk.ngrams(url_parse.path, 2)))
        trigramList = list(map(''.join, nltk.ngrams(url_parse.path, 3)))
        fourgramList = list(map(''.join, nltk.ngrams(url_parse.path, 4)))
        # Dicionários
        unigramDict = {x: 0 for x in unigramList}
        bigramDict = {x: 0 for x in bigramList}
        trigramDict = {x: 0 for x in trigramList}
        fourgramDict = {x: 0 for x in fourgramList}

        # Similaridade unigram
        if len(unigramDict) > 0:
            for i in unigramDict.keys():
                if i in Probabilidades:
                    SimFields['PathUnigram'] = SimFields['PathUnigram'] + Probabilidades[i]
            SimFields['PathUnigram'] = SimFields['PathUnigram'] / len(unigramDict)
        # Similaridade biggram
        if len(bigramDict) > 0:
            for i in bigramDict.keys():
                if i in Probabilidades:
                    SimFields['PathBigram'] = SimFields['PathBigram'] + Probabilidades[i]
            SimFields['PathBigram'] = SimFields['PathBigram'] / len(bigramDict)
        # Similaridade trigram
        if len(trigramDict) > 0:
            for i in trigramDict.keys():
                if i in Probabilidades:
                    SimFields['PathTrigram'] = SimFields['PathTrigram'] + Probabilidades[i]
            SimFields['PathTrigram'] = SimFields['PathTrigram'] / len(trigramDict)
        # Similaridade fourgram
        if len(fourgramDict) > 0:
            for i in fourgramDict.keys():
                if i in Probabilidades:
                    SimFields['PathFourgram'] = SimFields['PathFourgram'] + Probabilidades[i]
            SimFields['PathFourgram'] = SimFields['PathFourgram'] / len(fourgramDict)

    # ==========================> Parâmetros (params)
    if url_parse.params:
        #============================== Características de Tokens Dominio
        lista1 = nltk.tokenize.regexp_tokenize(url_parse.params,"[\w']+")
        lista2 = nltk.tokenize.regexp_tokenize(url_parse.params,"[\W']+")
        lista3 = {x:len(x) for x in lista1}
        lista4 = {x:len(x) for x in lista2}
        for i in lista4.items():
            lista3[i[0]] = i[1]
        #LISTA3 CONTEM TODOS OS TOKENS DAQUELA PARTE
        if len(lista3) > 0:
            SimFields['T_MT_P'] = max(lista3.values())
        #================================
    #     unigramList = list(map(''.join, nltk.ngrams(url_parse.params, 1)))
    #     bigramList = list(map(''.join, nltk.ngrams(url_parse.params, 2)))
    #     trigramList = list(map(''.join, nltk.ngrams(url_parse.params, 3)))
    #     fourgramList = list(map(''.join, nltk.ngrams(url_parse.params, 4)))
    #     # Dicionários
    #     unigramDict = {x: 0 for x in unigramList}
    #     bigramDict = {x: 0 for x in bigramList}
    #     trigramDict = {x: 0 for x in trigramList}
    #     fourgramDict = {x: 0 for x in fourgramList}

    #     # Similaridade unigram
    #     if len(unigramDict) > 0:
    #         for i in unigramDict.keys():
    #             if i in Probabilidades:
    #                 SimFields['ParamsUnigram'] = SimFields['ParamsUnigram'] + Probabilidades[i]
    #         SimFields['ParamsUnigram'] = SimFields['ParamsUnigram'] / len(unigramDict)
    #     # Similaridade biggram
    #     if len(bigramDict) > 0:
    #         for i in bigramDict.keys():
    #             if i in Probabilidades:
    #                 SimFields['ParamsBigram'] = SimFields['ParamsBigram'] + Probabilidades[i]
    #         SimFields['ParamsBigram'] = SimFields['ParamsBigram'] / len(bigramDict)
    #     # Similaridade trigram
    #     if len(trigramDict) > 0:
    #         for i in trigramDict.keys():
    #             if i in Probabilidades:
    #                 SimFields['ParamsTrigram'] = SimFields['ParamsTrigram'] + Probabilidades[i]
    #         SimFields['ParamsTrigram'] = SimFields['ParamsTrigram'] / len(trigramDict)
    #     # Similaridade fourgram
    #     if len(fourgramDict) > 0:
    #         for i in fourgramDict.keys():
    #             if i in Probabilidades:
    #                 SimFields['ParamsFourgram'] = SimFields['ParamsFourgram'] + Probabilidades[i]
    #         SimFields['ParamsFourgram'] = SimFields['ParamsFourgram'] / len(fourgramDict)

    return SimFields
