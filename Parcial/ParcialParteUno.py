# Calcula la tasa a la que un objeto cambia su rapidez. primero halla la diferencia obteniendo el incremento
# o perdida de la velocidad (restando la inicial a la final), y luego divide ese cambio entre el lapso transcurrido
# Anderson Geovanny Lopez Ramirez cod 0860206 - 2724
def calcularAceleracion(velocidadInicial,velocidadFinal, tiempoSegundos):
    
    while True:
        if velocidadFinal < 0 or velocidadInicial < 0  or tiempoSegundos < 0:
            print("Las Velocidades inicial y final y el tiempo no pueden ser < de 0")
            break
        else:
            tasaCambio = (velocidadFinal - velocidadInicial)/tiempoSegundos
            return tasaCambio
    
x = calcularAceleracion(2,-3,4)
print(x)