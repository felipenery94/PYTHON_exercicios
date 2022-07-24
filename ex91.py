import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mo site pudim não está acessivel no momento\033[m')
else:
    print('\033[33macessei o site pudim com sucesso\033[33m')
    print(site.read())

