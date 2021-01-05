import pygame
from termcolor import colored
pygame.init()
pygame.mixer.music.load("elevator.mp3")
pygame.mixer.music.play()
#from time import sleep




#print("Conecting in the server...")
#print("")

#sleep(2)
#print("Language detected Portuguese from Brazil...")
#print("")

#sleep(2)
#print("ABNT 2 Keyboard detected")
#print("")

#sleep(2)
#print("Translating for Portuguese from Brazil")
#print("")

#sleep(2)
#print("Sistema traduzido com sucesso!")
#print("")

print("Bem vindo ao Atlanta Pizza")
print('')
#numero_do_pais = 55
#ddd = 21
#numero = 990399220

#print("Algum problema? Ligue para este número +{} {} {}".format(numero_do_pais, ddd, numero))
print('')

number_of_pizzas = eval(input("Quantas pizzas você quer? "))

cost_per_pizza = eval(input("Quanto custa a pizza?"))

print("Você gostaria de Coca-Cola?")
print('''[1] Sim, eu Quero
[2]Não, Obrigado''')
opção = int(input("Qual è a sua opção?"))

if opção == 1:
    subtotals = number_of_pizzas * cost_per_pizza

    tax_rates = 0.08
    sales_taxs = subtotals * tax_rates

    beb = 12.45

    totals = subtotals + sales_taxs + beb

    print("O preço total é R${}".format(totals))
    print("Está incluso R${} pela pizza, R${} de taxa e R${} da Coca-Cola.".format(subtotals, sales_taxs, beb))
    sair = input("Para sair aperte a tecla [ENTER]")
    print(colored("Obrigado pela preferência ;P, sua pizza deve chegar em aproximadamente daqui a uma hora e trinta minutos ヾ(•ω•`)o", 'green')

elif opção == 2:
    subtotal = number_of_pizzas * cost_per_pizza

    tax_rate = 0.08
    sales_tax = subtotal * tax_rate

    total = subtotal + sales_tax

    print("O preço total é R${}".format(total))
    print("Está incluso R${} pela pizza e R${} de taxa.".format(subtotal, sales_tax))
    if (key === 'Enter'):
        print('Aperte Enter Para Sair')