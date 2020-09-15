#TESTE DE SITE - Ex. 114
#
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site inacessível.')
else:
    print('Site acessível.')
    print(site.read()) #pega o conteúdo html que está no site