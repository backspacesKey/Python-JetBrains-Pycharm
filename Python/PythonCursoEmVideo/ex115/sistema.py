from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "Cadastro_de_Pessoas.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

#cabeçalho('Sistema de Ariquivo do MS-ODS')
while True:
    resposta = menu(["Ver Pessoas cadastradas", 'Cadastrar Pessoas', 'Sair do Programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[33mSaindo do Sistema MS-ODS... Até Logo\033[m')
        sleep(2)
        break
    else:
        cabeçalho('\033[31m ERRO! Digite uma opção válida!\033[m')
    sleep(2)