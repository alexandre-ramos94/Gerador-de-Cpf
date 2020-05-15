from random import randint
from tkinter import *

def verifica():
    global lb
    lb['text'] = ''
    tot = x = 0
    teste = list()
    cp = str(ed.get())
    nb = cp[9]
    for c in cp:
        teste.append(int(c))
    for k in range(10, 1, -1):
        x += k * int(teste[tot])
        tot += 1
    if x % 11 == 0 or x % 11 == 1 and nb == 0 or int(nb) == (11 - (x % 11)):
       tot = x = 0
       nb2 = cp[10]
       for c in range(11, 1, -1):
           x += c * teste[tot]
           tot += 1
       if x % 11 == 0 or x % 11 == 1 and nb2 == 0 or int(nb2) == (11 - (x % 11)):
           lb['text'] = 'CPF válido'
       else:
           lb['text'] = 'CPF inválido'
    else:
        lb['text'] = 'CPF inválido'


def gerador():
    """Esta função gera os primeiros 9 numeros do cpf"""
    global lb
    lista = list()
    lb['text'] = ''
    h = ''
    for c in range(0, 9):
        h += str(randint(0,9))
    for c in h:
        lista.append(int(c))
    pridig(lista, lb)


def pridig(lst, lb):
    """esta função vai gerar os digitos verificadores"""
    # O primeiro digito
    x = cont = k = 0
    for c in range(10, 1, -1):
        x += c * lst[cont]
        cont += 1
    if x % 11 == 0 or x % 11 == 1:
        lst.append(0)
    else:
        lst.append(11 - (x % 11))
    cont = 0
    # O segundo dígito
    for c in range(11, 1, -1):
        k += c * lst[cont]
        cont += 1
    if k % 11 == 0 or k % 11 == 1:
        lst.append(0)
    else:
        lst.append(11 - (k % 11))
    mostra(lst, lb)


def mostra(lst, lb):
    lb['text'] = ''
    """Esta função mostra o numero final do cpf já formatado"""
    for t, v in enumerate(lst):
        if t == 2 or t == 5:
            lb['text'] += f'{v}.'
        elif t == 8:
            lb['text'] += f'{v}-'
        else:
            lb['text'] += f'{v}'
    lst.clear()

# Interface grafica básica usando o Tkinter
janela = Tk()
janela.title('Gerador de cpf')
janela.geometry('500x200')
lb = Label(janela, text='')
lb.pack()
bt = Button(janela, width=20, text='Gerar cpf', command=gerador)
bt.pack()
ed = Entry(janela, width="20")
ed.pack()
bt2 = Button(janela, width=20, text="teste", command=verifica)
bt2.pack()
janela.mainloop()








