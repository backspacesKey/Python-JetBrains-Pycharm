from tkinter import *

def bt_click() :
    import turtle
    t = turtle.Pen()
    turtle.bgcolor("black")
    sides = 4
    colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    for x in range(360):
        t.pencolor(colors[x%sides])
        t.forward(x * 3/sides + x)
        t.left(360/sides + 1)
        t.width(x*sides/200)
        t.speed(5)
    turtle.Terminator

janela = Tk()

bt = Button(janela, width=20, text="Clique Aqui.", command=bt_click )
bt.place(x=100, y=100)
lb = Label(janela,  text="teste")
lb.place(x=100, y=150)


janela.geometry("300x300+200+200")
janela.mainloop()
