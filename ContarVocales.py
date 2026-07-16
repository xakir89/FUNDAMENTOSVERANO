def contarvocales(texto):
    cont = 0
    vocales = "AEIOUaeiou"
    for letra in texto:
        for vocal in vocales:
            if letra == vocal:
                cont += 1 
    return cont
print(contarvocales("andersonandesmeralda"))