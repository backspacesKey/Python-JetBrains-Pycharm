print('')
l = float(input('\033[0;33;40mQual è A Largura Da Parede (em Metros): \033[m'))
print('')
c = float(input('\033[0;33;40mQual é o Comprimento da Parede (em Metros): \033[m'))

subtotal = l*c
total = subtotal / 2

print('')
print('\033[4;32;40mA dimensão da Parede é de {} x {} e a sua area é de {}m². Você Precisará de {:.2f}L de Tinta.\033[m'.format(l, c, subtotal, total))
