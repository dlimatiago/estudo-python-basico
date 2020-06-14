import urllib.request

try:
    url_status = urllib.request.urlopen("http://pudim.com.br").getcode()
except urllib.request.URLError:
    print('\033[31mO site não está acessível\033[m')
else:
    print('\033[34mConsegui acessá-lo\033[m')
