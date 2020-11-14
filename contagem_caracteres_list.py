'''Exercício de contagem de caracteres de uma string'''


def contar_caracteres(string):
    '''
    Conta os caracteres de uma string e apresenta em ordem alfabética.
    Ex.:
    >>>contar_caracteres("bruno")
    b: 1
    n: 1
    o: 1
    r: 1
    u: 1

    >>>contar_caracteres("banana")
    a: 3
    b: 1
    n: 2

    :param string: string
    '''

    caracteres = list(string)
    caracteres.sort()
    caracter = caracteres[0]
    contador = 1

    for i in caracteres[1:]:
        if i == caracter:
            contador += 1
        else:
            print(f"{caracter}: {contador}")
            caracter = i
            contador = 1
    print(f"{caracter}: {contador}")


print("bruno:")
contar_caracteres("bruno")
print("banana:")
contar_caracteres("banana")
