print('''################################
########Tinta de Parede ########
################################# ''')

print('')
l = float(input('\033[0;33;40mQual è A Largura Da Parede (em Metros): \033[m'))
print('')
c = float(input('\033[0;33;40mQual é o Comprimento da Parede (em Metros): \033[m'))
demão = int(input('\033[0;33;40mQuantas demãos de tinta serão necessárias? \033[m'))

pt = l*c
subtotal = pt / 2
total = subtotal * demão

print('')
print('\033[4;32;40mA dimensão da Parede é de {} x {} e a sua area é de {}m². Você Precisará de {:.2f}L de Tinta.\033[m'.format(l, c, pt, total))
