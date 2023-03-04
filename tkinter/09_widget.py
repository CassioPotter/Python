from tkinter import *

menu_inicial = Tk()
menu_inicial.title('primeiro app')

menu_inicial.geometry('500x500+500+100')
menu_inicial.resizable(True, True)
menu_inicial.minsize(100,100)
menu_inicial.maxsize(1000,1000)

menu_inicial.iconbitmap('projetos/icon.ico')
menu_inicial['bg'] = 'blue'


def cmd_Click():
    print('ola mundo')

def soma():
    print(f'A soma de 2 + 2 = {2+2}')

cmd = Button(menu_inicial, text='executar', command=cmd_Click)
cmd.pack()

btn = Button(menu_inicial, text='soma', command=soma)
btn.pack()



menu_inicial.mainloop()