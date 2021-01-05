from time import sleep

def main():
    nop = int(input('\033[0;33;40mQuantas Pizzas Você Quer? '))


    opção = int(input('As Opções de Pizza São: \n[1] Calabreza R$25,56 \n[2] Havaiana R$50,39\n[3]Frango c/ Catupiri R$46,32\n[4] Quatro Queijos R$44,44\n[5] Sair\n>>> \033[m'))

    if opção == 1:
        subtotal = nop * 25.56
        tax_rate = 0.08
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        print('\033[4;32;40m O Total é {:.2f}'.format(total))

    elif opção == 2:
        subtotal = nop * 50.39
        tax_rate = 0.08
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        print('\033[4;32;40mO Total é {:.2f}'.format(total))

    elif opção == 3:
        subtotal = nop * 46,32
        tax_rate = 0.08
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        print('\033[4;32;40mO Total é {:.2f}'.format(total))

    elif opção == 4:
        subtotal = nop * 44.44
        tax_rate = 0.08
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        print('\033[4;32;40mO Total é {:.2f}\033[m'.format(total))

    elif opção == 5:
        print('\033[1;34;40m Saindo...\033[m')

if __name__ == '__main__':
	main()

opç = int(input('Você Deseja Realizar Outra Operação? \n1. Sim \n2. Sair\n>>> '))

if opç == 1:
    main()

else:
    print('Saindo...')
    sleep(2)
    exit
