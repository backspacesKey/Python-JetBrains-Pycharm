def linha(tam = 58):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(58))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc



def leiaInt(msg):
    while True:
        try:
            j = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por Favor digite um número inteiro válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número')
            return 0
        try:
            return j
