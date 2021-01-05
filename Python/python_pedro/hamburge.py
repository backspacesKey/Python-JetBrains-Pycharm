print("Bem vindo ao Atlanta Hamburger")
print('')
numero_do_pais = 55
ddd = 21
numero = 990399220

#print("Algum problema? Ligue para este número +{} {} {}".format(numero_do_pais, ddd, numero))
print('')

number_of_hamburgers = eval(input("Quantos hamburgeres você quer? "))

cost_per_hamburgers = eval(input("Quanto custa o hamburger?"))

subtotal = number_of_hamburgers * cost_per_hamburgers

tax_rate = 0.08
sales_tax = subtotal * tax_rate
taxa_de_entrega = 10.90

total = subtotal + sales_tax + taxa_de_entrega

print("O preço total do hamburger é R${}".format(total))
print("Está incluso R${} pelo hamburger, R${} de taxa e R${} de taxa de entrega.".format(subtotal, sales_tax, taxa_de_entrega))
sair = input("Para sair aperte a tecla [ENTER]")
print("Obrigado pela preferência ;P, seu hamburger deve chegar em aproximadamente daqui a uma hora e trinta minutos ヾ(•ω•`)o")
