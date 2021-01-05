import PySimpleGUI as sg
from time import *
import json
class TelaPython():
    def __init__(self):
        #Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text("CEP"), sg.Input(key='cep')],
            [sg.Button("Enviar Os Dados"), sg.Button("Cancelar")]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)



        request = request.get(f'https://viacep.com.br/ws/{cep_input}/json/')

        adrees_data = request.json()
        print(adrees_data)
        # self.button, self.values = self.janela.Read()
    # def Iniciar(self):
    #     nome = self.values['nome']
    #     idade = self.values['idade']
    #     aceita_gmail = self.values['gmail']
    #     aceita_outlook = self.values['outlook']
    #     aceita_yahoo = self.values['yahoo']
    #     aceita_cartao = self.values['simaceitacartao']
    #     nao_aceita_cartao = self.values['naoaceitacartao']
    #     print(f'Nome: {nome}')
    #     print(f'Idade: {idade}')
    #     print(f'Aceita Gmail: {aceita_gmail}')
    #     print(f'Aceita Outlook: {aceita_outlook}')
    #     print(f'Aceita Yahoo: {aceita_yahoo}')
    #     print(f'Aceita Cartão: {aceita_cartao}')
    #     print(f'Não Aceita Cartão: {nao_aceita_cartao}')


tela = TelaPython()
tela.Iniciar()

