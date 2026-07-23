def factorial(numero):
    if numero == 1 :
        return 1
    else:
        resultado = numero * factorial(numero-1)
        return resultado
    
re = factorial(5)
print (re)



def suma(numero):
    pos = len(numero)
    if pos == 0:
        return 0
    else:
        sumar = numero[0] + suma(numero[1:pos])
        return sumar
    
lista=[1,3,4,6]
su = suma(lista)
print(su)
    