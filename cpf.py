from random import randint
from tkinter import *


def iguais(lst, lb):
    ok = False
    cont = 1
    for c in range(0, len(lst) - 1):
        if lst[c] == lst[cont]:
            ok = True
            cont += 1
        else:
            ok = False
            break
    if ok:
        lb['text'] = 'Um cpf com todos os números iguais não é válido, tente novamente'
    else:
        pass
    return ok


def personaliza():
    global lb
    try:
        pers = list()
        cp = ed2.get().replace('.', '').strip().replace(' ', '')
        if len(cp) == 9:
            for c in cp:
                pers.append(int(c))
            pridig(pers, lb)
        else:
            lb['text'] = 'Por favor digite apenas 9 números válidos'
    except:
        lb['text'] = 'Houve problemas com os dados, digite 9 numeros válidos'


def verifica():
    """Esta função irá verificar a validade de um número de cpf baseado em principios matemáticos"""
    global lb
    try:
        lb['text'] = ''
        tot = x = p =0
        teste = list()
        cp = str(ed.get().replace('.', '').replace('-', '').strip().replace(' ', ''))
        if len(cp) < 12:
            nb = cp[9]
            for c in cp:
                teste.append(int(c))
            veri = iguais(teste, lb)
            if not veri:
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
                       for c in teste:
                           p += 1
                           if p == 3 or p == 6:
                               lb['text'] += f'{str(c)}.'
                           elif p == 9:
                               lb['text'] += f'{str(c)}-'
                           else:
                               lb['text'] += f'{str(c)}'
                       lb['text'] += f': CPF Válido'
                   else:
                       lb['text'] = 'CPF inválido'
                else:
                    lb['text'] = 'CPF inválido'
            else:
                pass
        else:
            lb['text'] = 'Um numéro de cpf válido deve conter 11 numeros'
    except:
        lb['text'] = 'Houve algum problema com os dados, verifique-os e tente novamente'


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
    veri = iguais(lst, lb)
    if not veri:
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
bt2 = Button(janela, width=20, text="Verificar nº de cpf", command=verifica)
bt2.pack()
ed = Entry(janela, width=23)
ed.pack()
bt3 = Button(janela, width=20, text='Gerar cpf personalizado', command=personaliza)
bt3.pack()
ed2 = Entry(janela, width=23)
ed2.pack()
lb3 = Label(janela, text="Digite 9 números válidos para gerar um cpf personalizado")
lb3.pack()


janela.mainloop()








