'''Exercício de contagem de caracteres de uma string'''


def contar_caracteres(string):
    '''
    Conta os caracteres de uma string e apresenta em ordem alfabética.
    Ex.:
    >>>contar_caracteres("bruno")
    {'b': 1, 'n': 1, 'o': 1, 'r': 1, 'u': 1,}

    >>>contar_caracteres("banana")
    {'a': 3, 'b': 1, 'n': 2,}

    :param string: string
    '''

    result = {}

    for caracter in string:
        result[caracter] = result.get(caracter, 0) + 1

    print(result)


print("bruno:")
contar_caracteres("bruno")

print("banana:")
contar_caracteres("banana")
