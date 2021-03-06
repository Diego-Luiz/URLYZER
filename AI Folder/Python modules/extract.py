from urllib.parse import urlparse
import csv
import os
import tldextract
import ngramExtract
'''
    => How the URL is being represented
'''
URL= ['URL', 'T_U', 'Q_L_U', 'Q_N_U', 'Q_T_U', 'Q_CHARNALPHA', 'T_MT_U', 'T_DOM', 
    'C_IP', 'T_TL', 'T_SL', 'T_MT_DOM', 'Q_V', 'DOM_TK_1', 'DOM_TK_2', 'DOM_TK_3', 'DOM_TK_4', 
    'DOM_TK_5', 'DOM_TK_6', 'DOM_TK_7', 'DOM_TK_8', 'DOM_TK_9', 'DOM_TK_10', 'DOM_TK_11', 'DOM_TK_12',
    'DOM_TK_13', 'DOM_TK_14', 'DOM_TK_15', 'DOM_TK_16', 'DOM_TK_17', 'T_CM', 'T_MT_CM', 'T_DIR', 
    'Q_DIR', 'DIR_TK_1', 'DIR_TK_2', 'DIR_TK_3', 'DIR_TK_4', 'DIR_TK_5', 'DIR_TK_6', 'DIR_TK_7',
    'DIR_TK_8', 'DIR_TK_9', 'DIR_TK_10', 'DIR_TK_11', 'DIR_TK_12', 'DIR_TK_13', 'DIR_TK_14', 'DIR_TK_15', 
    'DIR_TK_16', 'DIR_TK_17', 'T_A', 'E_EXE', 'E_ZIP', 'E_PHP', 'E_R', 'E_DLL', 'A_TK_1', 'A_TK_2', 'A_TK_3', 
    'A_TK_4', 'A_TK_5', 'A_TK_6', 'A_TK_7', 'A_TK_8', 'A_TK_9', 'A_TK_10', 'A_TK_11', 'A_TK_12', 'A_TK_13', 'A_TK_14',
    'A_TK_15', 'A_TK_16', 'A_TK_17', 'T_P', 'T_MT_P', 'P_TK_1', 'P_TK_2', 'P_TK_3', 'P_TK_4', 'P_TK_5', 'P_TK_6', 'P_TK_7',
    'P_TK_8', 'P_TK_9', 'P_TK_10', 'P_TK_11', 'P_TK_12', 'P_TK_13', 'P_TK_14', 'P_TK_15', 'P_TK_16', 'P_TK_17', 'URLUnigram', 
    'URLBigram', 'URLTrigram', 'URLFourgram', 'HostUnigram', 'HostBigram', 'HostTrigram', 'HostFourgram', 'PathUnigram', 'PathBigram', 
    'PathTrigram', 'PathFourgram', 'Label'
]
#Vowels
Vogais = ['a','e','i','o','u','A','E','I','O','U']
#Extensions
Extensoes = ['EXE','ZIP','PHP','R','DLL']
'''
Function responsible for extracting the characteristics about the tokens given a determinated string.
    -prefixo: The character prefix in the URL's dictionary (DOM, DIR, A, P), related to the string (what part of it)
    -dicionario: Corresponding to the URL's python dictionary
    -string: The URL part sent to be tokenized (Domain, directory, archive, parameters)
'''
def tokens(prefixo, dicionario, string):
    posicao = prefixo +'_'
    
    dicionario[posicao+'TK_1'] = string.count('.')
    dicionario[posicao+'TK_2'] = string.count('?')
    dicionario[posicao+'TK_3'] = string.count('!')
    dicionario[posicao+'TK_4'] = string.count('+')
    dicionario[posicao+'TK_5'] = string.count('%')
    dicionario[posicao+'TK_6'] = string.count('-')
    dicionario[posicao+'TK_7'] = string.count('=')
    dicionario[posicao+'TK_8'] = string.count('()')
    dicionario[posicao+'TK_9'] = string.count('*')
    dicionario[posicao+'TK_10'] = string.count('_')
    dicionario[posicao+'TK_11'] = string.count('@')
    dicionario[posicao+'TK_12'] = string.count('~')
    dicionario[posicao+'TK_13'] = string.count('#')
    dicionario[posicao+'TK_14'] = string.count('/')
    dicionario[posicao+'TK_15'] = string.count('&')
    dicionario[posicao+'TK_16'] = string.count(',')
    dicionario[posicao+'TK_17'] = string.count('$')

'''
Function responsible for extracting most of the URL's lexical features given the Input archive (ArqEntrada)
-ArqEntrada: The input file with the URLs
-ArqSaida: The output file with the URLs and its characteristics extracted
'''
def execute(ArqEntrada,ArqSaida):
     
    with open(ArqSaida,'w',newline='',encoding='Latin1') as extracted:
        csv_writer = csv.DictWriter(extracted,fieldnames=URL)
        csv_writer.writeheader()#Gravar os indices no arquivo
        
        with open(ArqEntrada,'r',encoding='Latin1') as urls:
            csv_reader = csv.reader(urls) #iterador sobre o arquivo
            csv_reader.__next__() #p/nao ler o indice
            Probabilidades = ngramExtract.readProbabilities()
            for url_list in csv_reader:
                URL_= {x:0 for x in URL}
                url_string = url_list[0] #pegando a string corresponde a URL dentro da lista naquela posicao
                
                if url_string[0:2] == '//':
                    url_string = url_string[2:]
                URL_['URL'] = url_string
                
                # ==>> URL COMPLETA
                URL_['T_U'] = len(url_string) 
                #Quantidade de letras
                qtd_letras = 0
                for i in url_string:
                    if i.isalpha():
                        qtd_letras = qtd_letras + 1
                URL_['Q_L_U'] = qtd_letras
                # #Quantidade de numeros
                qtd_num = 0
                for i in url_string:
                    if i.isnumeric():
                        qtd_num = qtd_num + 1
                URL_['Q_N_U'] = qtd_num
                # Quantidade de caracteres n??o alpha num??ricos
                qtd_alnum = 0
                for i in url_string:
                    if not i.isalnum():
                        qtd_alnum = qtd_alnum + 1
                URL_['Q_CHARNALPHA'] = qtd_alnum

                url_parse = urlparse(url_list[0]) #pegando os atributos da url (dominio, parametros, caminho, etc)
                
                # ==>> DOM??NIO (netloc)
                URL_['T_DOM'] = len(url_parse.netloc) 
                #Verificar se o dominio nao ?? IP, true (1) se for e false (0) se n??o for
                qtd = 0
                flag = 0
                for i in url_parse.netloc:
                    if i.isnumeric() or i=='.':
                        qtd= qtd + 1
                if qtd == len(url_parse.netloc):
                    flag = 1
                URL_['C_IP'] = flag
                ##
                partes_dominio = tldextract.extract(url_string)
                #Tamanho do Top-Level Domain
                URL_['T_TL'] = len(partes_dominio.suffix)
                #Tamanho do Second-Level Domain
                URL_['T_SL'] = len(partes_dominio.domain)
                #Quantidade de Vogais
                qtd_vogais = 0
                for i in url_parse.netloc:
                    if i in Vogais:
                        qtd_vogais = qtd_vogais + 1 
                URL_['Q_V'] = qtd_vogais


                #Caracter??sticas de tokens
                tokens('DOM',URL_, url_parse.netloc)
                
                # ==>> Caminho (url_parse.path)
                if url_parse.path and url_parse.path!='/': #se tiver caminho e se for realmente um caminho: mais coisa q /
                    #print('Aqui: {}'.format(url_parse.path))
                    URL_['T_CM'] = len(url_parse.path)
                    # ==>> Diret??rio ( os.path.dirname(url_parse.path) )
                    URL_['T_DIR'] = len(os.path.dirname(url_parse.path))
                    #Quantidade diret??rios
                    lista = url_parse.path.split('/')
                    URL_['Q_DIR'] = len(lista) - 1 
                    #
                    tokens('DIR',URL_,os.path.dirname(url_parse.path))
                    # ==>> Arquivo ( os.path.basename(url_parse.path) )
                    if os.path.basename(url_parse.path):
                        URL_['T_A'] = len(os.path.basename(url_parse.path))
                        nome, extensao = os.path.splitext(os.path.basename(url_parse.path))
                        if extensao: #se tiver extens??o
                            #Pegando o nome da extens??o e convertendo em maiusculo p/ser compat??vel com a lista 'Extensoes'
                            extensao = extensao.split('.')[1].upper()
                            if extensao in Extensoes:
                                URL_['E_'+extensao] = 1
                        #Caracter??sticas de tokens
                        tokens('A',URL_,os.path.basename(url_parse.path))
                    # ==>> Par??metros (url_parse.params)
                    if url_parse.params:
                        URL_['T_P'] = len(url_parse.params)
                        tokens('P',URL_,url_parse.params)
                #N-grams characteristics
                URL_.update(ngramExtract.extractFeatures(url_list[0],Probabilidades))
                URL_['Label'] = url_list[1]   
                csv_writer.writerow(URL_)
