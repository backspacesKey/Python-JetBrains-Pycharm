import urllib
import urllib.request
from colorama import *

try:
    ns = input("Qual é o Nome do Site: ")
    site = urllib.request.urlopen(input("Qual é a URL: "))
except:
    print(f'O site não está acessivel no momento.')
else:
    print(f'O site {ns} está acessivel no momento.')
