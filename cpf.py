from random import randint


def gerador():
    """Esta função gera os primeiros 9 numeros do cpf"""
    h = ''
    for c in range(0, 9):
        h += str(randint(0,9))
    return h


def pridig(lst):
    """esta função vai gerar os digitos verificadores"""
    # O primeiro digitp
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
        k += c * lista[cont]
        cont += 1
    if k % 11 == 0 or k % 11 == 1:
        lista.append(0)
    else:
        lista.append(11 - (k % 11))


def mostra(lst):
    """Esta função mostra o numero final do cpf já formatado"""
    print('Cpf gerado: ', end='')
    for t, v in enumerate(lst):
        if t == 2 or t == 5:
            print(f'{v}.', end='')
        elif t == 8:
            print(f'{v}-', end='')
        else:
            print(v, end='')


lista = list()
cpf = gerador()
# Vamos adicionar os 9 valores dentro da lista final
for c in cpf:
    lista.append(int(c))
# Agora precisamos gerar os "digitos verificadores", os dois ultimos do cpf
pridig(lista)
# E por último chamamos a função para montar o cpf formatado
mostra(lista)







