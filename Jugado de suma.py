print()
jugadores = int(input("Ingrese Numero de jugadores: "))
#rondas = 2
print()
#punto_cierre = 12
puntos = 0
#for j in range(1,rondas+1):
#    print(f"Ronda {j}")
print()
i=0
while i < jugadores:
    if puntos == 12:
        i = 0
    if i % 2 != 0:
        puntos -= 1
        print(f"Jugador {i} = Resta Puntos: {puntos}")
    elif i % 2 == 0:
        puntos += 2
        print(f"Jugador {i} = Suma Puntos: {puntos}")
    
    i = i + 1
print()

    
        