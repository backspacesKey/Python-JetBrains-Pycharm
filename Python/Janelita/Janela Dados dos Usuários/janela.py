import PySimpleGUI as sg
from time import *
class TelaPython():
    def __init__(self):
        #Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text("Nome"), sg.Input(key='nome')],
            [sg.Text("Idade"), sg.Input(key='idade')],
            [sg.Text('Qual os provedores de e-mail você aceita?')],
            [sg.Checkbox("Gmail", key='gmail'), sg.Checkbox("Outlook", key='outlook'), sg.Checkbox("Yahoo", key='yahoo')],
            [sg.Text("Você aceita cartões?")],
            [sg.Radio('Sim', 'cartoes', key='simaceitacartao'), sg.Radio('Não', 'cartoes', key='naoaceitacartao')],
            [sg.Button("Enviar Os Dados"), sg.Button("Cancelar")]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        self.button, self.values = self.janela.Read()
    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        aceita_gmail = self.values['gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['yahoo']
        aceita_cartao = self.values['simaceitacartao']
        nao_aceita_cartao = self.values['naoaceitacartao']
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Aceita Gmail: {aceita_gmail}')
        print(f'Aceita Outlook: {aceita_outlook}')
        print(f'Aceita Yahoo: {aceita_yahoo}')
        print(f'Aceita Cartão: {aceita_cartao}')
        print(f'Não Aceita Cartão: {nao_aceita_cartao}')


tela = TelaPython()
tela.Iniciar()

