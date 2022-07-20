import requests

from time import sleep


def main():
    print('')
    print('\033[0;33;40m#####################')
    print('## Consulta de CEP ##')
    print('#####################')
    print('')

    cep_input = input('Digite o Cep Com 8 Dígitos: \033[m')
    if len(cep_input) > 8:
        print(
            '\033[0;31;40m Erro 0001: O CEP digitado contém mais de 8 dígitos.\033[m')
        print('\033[1;34;40mTentando Novamente\033[m')
        sleep(3)
        main()

    if len(cep_input) < 8:
        print(
            '\033[0;31;40m Erro 0001: O CEP digitado contém menos de 8 dígitos.\033[m')
        print('\033[1;34;40mTentando Novamente\033[m')
        sleep(3)
        main()

    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')

    adrees_data = request.json()

    if 'erro' not in adrees_data:
        print('Procurando...')
        sleep(2)
        print('\033[4;32;40m==> CEP Encontrado <==')
        print('CEP: {}'.format(adrees_data['cep']))
        sleep(1)
        print('Rua: {}'.format(adrees_data['logradouro']))
        sleep(1)
        print('Complemento: {}'.format(adrees_data['complemento']))
        sleep(1)
        print('Bairro: {}'.format(adrees_data['bairro']))
        sleep(1)
        print('Cidade e UF: {} & {}'.format(
            adrees_data['localidade'], adrees_data['uf']))
        sleep(1)
        print('DDD: {}\033[m'.format(adrees_data['ddd']))
        print('')
        # print(requests.json())

    else:
        print(f'{cep_input}: O CEP Dígitado não é um lugar.')

    print('----'*5)
    opção = int(
        input('Você Deseja Realizar Outra Operação? \n1. Sim \n2. Sair\n>>> '))

    if opção == 1:
        main()
    if opção == 2:
        print('\033[0;34;40m Saindo...\033[m')
        exit()


if __name__ == '__main__':
    main()
