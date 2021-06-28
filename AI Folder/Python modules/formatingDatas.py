import csv
'''
Function responsible for formating the URLs that don't have their Internet Protocol
-ArqLeitura: the input file  
'''
def format(ArqLeitura):
    protocolos = ['HTTP','HTTPS','FTP','http','https','ftp']
    Indices = ['URL','Label'] #the indexes that the input file must have
    URL = {'URL':'','Label':0}
    with open(ArqLeitura+'Formated.csv','w',newline='',encoding='Latin1') as ArqSaida:
        csv_writer = csv.DictWriter(ArqSaida,fieldnames=Indices)
        csv_writer.writeheader()
        with open(ArqLeitura+'.csv','r',encoding='Latin1') as ArqLeit:
            csv_reader = csv.reader(ArqLeit)
            csv_reader.__next__()
            for url_list in csv_reader:
                if url_list:
                    url = url_list[0]
                    URL['URL'] = url
                    URL['Label'] = int(url_list[1])
                    result = url.split(':')
                    if result[0] not in protocolos:
                        URL['URL'] = '//'+url
                    
                    csv_writer.writerow(URL)