def suma(numero):
    if numero <= 1:
        return 1
    else:
        return numero + suma(numero-1)
suma(3)


def sumarDigitos(numero):
    if numero <= 1:
        return 1
    else:
        return numero%10 + sumarDigitos(numero//10)
print(sumarDigitos(1422))

def imprimeDigitos(numero):
    if numero <= 0: return
    print (numero, end=' ')
    imprimeDigitos(numero-1)
imprimeDigitos(5)
print()
def imprimeDigitosInvertido(numero):
    if numero <= 0: return 
    imprimeDigitosInvertido(numero-1)
    print (numero, end=' ')
imprimeDigitosInvertido(5)