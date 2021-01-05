# Adicionando alguns pacotes
from time import sleep


# Definindo Algumas Variáveis
# def msgObrigado():

#     print("Obrigado Por Comprar na Atlanta Pizza 😀")
#     sleep(2)
#     print("Volte Sempre. A Atlanta Pizza Agradece a Sua Visita 😹🎉")



#     print(Fore.GREEN)

# def :
#     print(Fore.YELLOW)

# def:
#     print(Fore.WHITE)

# Coletando os Dados

seu_nome = input('\033[0;33;40mQual é o seu nome? ')
number_of_pizzas = eval(input(f'Qual a Quantidade de pizzas que você quer {seu_nome}? '))
cost_per_pizzas = eval(input(f"Quanto custa a pizza {seu_nome}?\033[m "))



# Definindo e Fazendo as operações matemática
subtotal = number_of_pizzas * cost_per_pizzas
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + tax_rate

# Falando os Resultados

print(f'\033[0;33;40mO total é de {total}')
sleep(3)
print(f'A pizza custa R${subtotal} e o Trabalho que dá {sales_tax}')
sleep(3)
# print(f'Como dito a forma de pagamento é de {pag}')
sleep(3)
# msgObrigado()
print('\033[m')
