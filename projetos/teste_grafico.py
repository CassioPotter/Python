from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Input(key = 'mensagem')],
    
]

#janela
janela = sg.Window('TELA DE MENSAGEM')

#evento
while True:
    eventos = janela.read()
    if eventos == sg.WINDOW_CLOSE:
        break
    if eventos == Mensagem:
        print('ola mundo')
    
window.closed()
