from tkinter import *

top = Tk()
L1 = Label(top, text = "Quantas Pizzas Você quer?")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

L2 = Label(top, text = "Qual o preço da pizza?")
L2.pack( side = RIGHT)
E2 = Entry(top, bd = 5)
E2.pack(side = LEFT)

print(L2)
top.mainloop()