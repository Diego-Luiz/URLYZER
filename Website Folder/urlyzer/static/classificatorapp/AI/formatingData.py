def execute(Url):
    protocolos = ['HTTP','HTTPS','FTP','http','https','ftp']
    URL = Url
    result = Url.split(':')
    if result[0] not in protocolos:
        URL = '//'+Url
    
    return URL