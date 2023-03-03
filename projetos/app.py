from tkinter import *

menu_inicial = Tk()
menu_inicial.title('primeiro app')

menu_inicial.geometry('500x500+1+1')
menu_inicial.resizable(False,False)

menu_inicial.iconbitmap('projetos\icon.ico')
menu_inicial ['bg'] = 'blue'

def btn_clic (mensagem):
    print(mensagem)

btn = Button(menu_inicial, text='executar', command = lambda:btn_cliC('OLA MUNDO'))
btn.pack()


menu_inicial.mainloop()
