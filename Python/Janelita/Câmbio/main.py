import requests
import json
print(' ')
# print(' ')

real = float(input('Quanto Você quer Converter? R$'))

print('Agora, Escolha Para Qual Moeda Você quer converter.(Digite O número dele.)')
opção = 0
while opção != 7:
    print('''[1] Dólar
[2] Iene
[3] Euro
[4] Outro
[5] Dólar > Real
[6] Novo Número
[7] Sair do Programa''')
    opção = int(input('>>> '))
    if opção == 1:
        dolar = real / 5.56
        print('O Resultado Da Conversão é igual a ${:.2f}'.format(dolar))

    elif opção == 2:
        iene = real / 0.050
        print('O Resultado Da Conversão é igual a ¥{:.2f}'.format(iene))

    elif opção == 3:
        euro = real / 6.32
        print('O Resultado Da Conversão é igual a €{:.2f}'.format(euro))

    elif opção == 4:
        nome = input('Qual é O Nome da Moéda? ')
        outro = float(input(f'Quanto Custa 1 {nome} no tipo da moêda que você deseja.(Não Coloque o Símbolo da Moeda.): '))
        tot = real / outro
        print('A Conversão é Igual à {:.2f} {}'.format(tot, nome))

    elif opção == 5:
        tott = real * 5.16
        print('A Conversão é igual á {:.2f}'.format(tott))
    elif opção == 6:
        print('Ok, Informe os Valores Novamente:')
        real = float(input('Quanto Você quer Converter? R$'))
    elif opção == 7:
        print('FINALIZANDO...')
    else:
       print('Tente Novamente!')
    print('=-=' * 25)
print('Fim do Programa 🎇')
