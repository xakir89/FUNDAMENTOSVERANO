compuertas = ['A','P','R','A','P','R']
e0 = float(input("Eneria inicial en Joules (J): "))
Eimp = float(input("Energia de impulso: "))
Efreno = float(input("Energia de Freno: "))

particula_viva = True
motivo_parada = ""
compuerta_actual = 0

while compuerta_actual < len(compuertas) and particula_viva:
    tipo = compuertas[compuerta_actual]
    compuerta_actual = compuerta_actual + 1
    num_paso = compuerta_actual + 1

    print(f"\n[Compuerta #{num_paso} - {tipo}]")
    print(f" > ENERGIA AL ENTRAR: {e0:.2f}")

    if tipo =='A':      
# COMPUERTA TIPO A (ACELERADORA)
        if 0 < e0 < 15:
            Energia_actual = e0+(Eimp * 0.5)
            print(f"Perdida de Eficiencia del 50% {Energia_actual}")
        elif e0 > 15:
            Energia_actual = e0 + Eimp
            print(f"Incrementa la Energia de la Particula {Energia_actual}")
        else:
            print("La particula se quedo sin energia y para completamente")
            break
# COMPUERTA TIPO P (PASIVA / FRENO)
    elif tipo == 'P':
        if 1.0 <= Energia_actual <= 5.0:
            print("Zona de Resonancia Destructiva no se puede avanzar")
            break
        else: 
            Energia_actual = Energia_actual - Efreno
            print(f"Enerigia atual menos la Energia de Freno: {Energia_actual}")
# COMPUERTA TIPO R (RESONANTE)
    elif tipo == 'R':
        if Energia_actual % 2 == 0:
            amplificacion = Energia_actual * 1.2
            print(f"factor de Amplificacion: {amplificacion}")
        else:
            Energia_actual = Energia_actual - 5.0
            print(f"Penalizacion - 5.0 J: {Energia_actual}")
    

# Parada y Fallo del Sistema 

#

    