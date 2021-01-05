import urllib
import urllib.request
import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome Do Site: '),sg.Input(key='ns')],
    [sg.Text('URL do Site: '),sg.Input(key='us')],
    [sg.Button('Verificar')]
]

janela = sg.Window("URL do Site", layout)

try:
    site = 