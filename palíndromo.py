def longitud(texto):
    cont = 0
    for letra in texto:
        cont += 1
    return cont
def reconocer(palabra):
    inicio = 0
    fin = longitud(palabra) - 1
    while inicio < fin:
        print(inicio,palabra[inicio],palabra[fin],fin)
        if palabra[inicio] != palabra[fin]:
            
            return False
        inicio += 1
        fin -= 1
    return True
def reconocerr(palabra):
    fin = longitud(palabra)-1
    for inicio in range(0,fin//2):
        print(inicio, palabra[inicio], palabra[fin - inicio ], fin - inicio )
        if palabra[inicio] != palabra[fin - inicio]:
            return False
    return True

print("reconocer es paralilogramo",reconocerr("reconocer"))