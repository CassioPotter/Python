from tkinter import *

menu_inicial = Tk()
menu_inicial.title('primeiro app')

menu_inicial.geometry('500x500')
menu_inicial.resizable(True, True)
menu_inicial.minsize(100,100)

menu_inicial.iconbitmap('projetos/icon.ico')
menu_inicial['bg'] = 'blue'


def cmd_Click():
    print('ola mundo')

def soma():
    print(f'A soma de 2 + 2 = {2+2}')

cmd = Button(
    menu_inicial, 
    text='executar', 
    command=cmd_Click
    )
cmd.pack()

btn = Button(
    menu_inicial, 
    text='soma', 
    command=soma
    )
btn.pack()  

label1 = Label(
                menu_inicial,
                text='''Esse é o label 1
                texto 2
                texto 3
                texto 4''', 
                bg= 'red',
                fg='white',
                font='Arial 42 bold italic',
                width=100
                )
label1.pack()

























menu_inicial.mainloop()