def suma(numero):
    if numero <= 1:
        return 1
    else:
        return numero + suma(numero-1)

def sumarDigitos(numero):
    if numero <= 1:
        return 1
    else:
        return numero%10 + sumarDigitos(numero//10)

def imprimeDigitos(numero):
    if numero <= 0: return
    print (numero, end=' ')
    imprimeDigitos(numero-1)

def imprimeDigitosInvertido(numero):
    if numero <= 0: return 
    imprimeDigitosInvertido(numero-1)
    print (numero, end=' ')


# Ejercicio 2: Calcular la potencia de un número (base^exponente)
# Pista: Cualquier número elevado a la potencia 0 es 1.

def potencia(base, exponente):
# Escribe aquí tu Caso Base
    if exponente==0:
        return 1
#Caso Recursivo
    elif exponente < 0 :
        return 1 / base * potencia(base, exponente + 1)
    return base * potencia(base, exponente - 1)
#print(potencia(2,-2))

# Ejercicio 3: Contar las vocales de una palabra Pista: Evalúa si la primera letra es vocal, 
# suma 1 (o 0 si no lo es), y pásale a la función el resto de la palabra.

def contar_vocales(palabra):
    #Caso Base (palabra vacía)
    if len(palabra) == 0:
        return 0
    #Lógica y Caso Recursivo
    es_vocal = 1 if palabra[0] in "aeiouAEIOU" else 0
    return es_vocal + contar_vocales(palabra[1:])
#print(contar_vocales('amore'))

def paginas(libros):
    if len(libros ) == 0:
        return 0
    return libros[0] + paginas(libros[1:])
#print(paginas([50,100,150,50]))

def factorial2(numero):
    if numero == 0:
        return 1
    return numero * factorial2(numero-1)
#print(factorial2(100))

# invertir Texto
def inversionTexto(palabra):
    if palabra == '' : return ''
    return inversionTexto(palabra[1:]) + (palabra[0])    
#print(inversionTexto('paparapa'))

# La Sucesión de Fibonacci: Cada número es la suma de los dos anteriores. (0, 1, 1, 2, 3, 5, 8...).
# Para calcular el 4to, necesito el 3ro y el 2do a la vez.
def fibonacci(numero):
    if numero == 0: return 2 #caso base 1
    if numero == 1: return 4 #caso base 2
    return fibonacci(numero-1) + fibonacci(numero-2) 
def serieFibonacci(numero,iteracion=0):
    if iteracion > numero: return
    print(fibonacci(iteracion),end=' ')
    serieFibonacci(numero, iteracion +1)


serieFibonacci(5,)
