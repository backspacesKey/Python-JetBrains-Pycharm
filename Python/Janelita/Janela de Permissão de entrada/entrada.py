from PySimpleGUI import PySimpleGUI as sg
from colorama import *
from time import *
#from playsound import playsound


#Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Usuario:"), sg.Input(key='usuario', size=(46, 1))],
    [sg.Text("Senha:"), sg.Input(key='senha',password_char='*', size=(47, 1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar'),sg.Button('Cancelar')]
]
#janela
janela = sg.Window("Permissão de Entrada", layout)
#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == 'Cancelar':
        print(Fore.RED + 'Encerrando o programa...')
        sleep(1)
        print(Fore.RED + 'Encerrado')
        break
    if eventos == sg.WINDOW_CLOSED:
        print(Fore.RED + 'Encerrando o programa...')
        sleep(1)
        print(Fore.RED + 'Encerrado')
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Pedro Luiz' and valores['senha'] == 'PASSWORD':
            sg.popup("ENTRADA APROVADA, PEDRO ESTA PERMITIDO ENTRAR NA CASA MEDEIROS.")
            sleep(0.1)
            break
        elif valores['usuario'] == 'Rafael' and valores['senha'] == 'Rafael':
            sg.popup('ENTRADA APROVADA, RAFAEL ESTA PERMITIDO ENTRAR NA CASA MEDEIROS.')
            sleep(0.1)
            break
        elif valores['usuario'] == 'Sergio' and valores['senha'] == 'Sergio':
            sg.popup('ENTRADA APROVADA, SERGIO ESTA PERMITIDO ENTRAR NA CASA MEDEIROS.')
            sleep(0.1)
            break
        elif valores['usuario'] == 'Ana Luiza' and valores['senha'] == 'Ana':
            sg.popup('ENTRADA APROVADA, ANA LUIZA ESTA PERMITIDO ENTRAR NA CASA MEDEIROS.')
            sleep(0.1)
            break
        elif valores['usuario'] == 'Maria Da Luz' and valores['senha'] == 'Maria':
            sg.popup('ENTRADA APROVADA, MARIA DA LUZ ESTA PERMITIDO ENTRAR NA CASA MEDEIROS.')
            sleep(0.1)
            break
        elif valores['usuario'] == 'Zete' and valores['senha'] == 'Zete':
            sg.popup('ENTRADA APROVADA, MARIZETE ESTÁ PERMITIDA ENTRAR NA CASA MEDEIROS.')
            sleep(0.1)
            break
        else:
            sg.popup('LOGIN INCORRETO. REESCREVA O SEU LOGIN CORRETAMENTE.')
            sleep(0.58)
            break
#FIM DO CÓGIGO
