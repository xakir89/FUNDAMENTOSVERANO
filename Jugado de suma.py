import sys
import time
def inputs(s):
    while True:
        try:
            opc = int(input(s)) 
            print("...")
            break
        except ValueError:
            print(f"Error entrada no valida solo puede ingresar números")
            print("...")
    return opc

def animacionPar():
    #doble barra \ para que Python imprima una sola \
    frames = [
        "🤜🏻🏈          🦵🏻",
        "🤜🏻  🏈        🦵🏻",
        "🤜🏻    🏈      🦵🏻",
        "🤜🏻      🏈    🦵🏻",
        "🤜🏻        🏈  🦵🏻",
        "🤜🏻          🏈🦵🏻",
    ]
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.1)    # Pausa de 0.2 segundos por fotograma
    print()


def animacionImpar():
    #doble barra \ para que Python imprima una sola \
    
    frames = [
        f"{'🤜🏻          🏈🦵🏻':>62}",
        f"{'🤜🏻        🏈  🦵🏻':>62}",
        f"{'🤜🏻      🏈    🦵🏻':>62}",
        f"{'🤜🏻    🏈      🦵🏻':>62}",
        f"{'🤜🏻  🏈        🦵🏻':>62}",
        f"{'🤜🏻🏈          🦵🏻':>62}",
    ]
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.1)    # Pausa de 0.2 segundos por fotograma
    print()

def animacionFin():
    print()
    frames = [
        f"{'🏁':^68}",
        f"{'🏁 ✨':^68}",
        f"{'🏁 ✨ ✨':^68}",
        f"{'🏁 ✨ ✨ ✨':^68}",
        f"{'🏁 ✨ ✨ ✨ ✨ ✨':^68}",
        f"{'🏁 ✨ ✨ ✨ ✨ ✨ ✨':^68}",
        f"{'🏁 ✨ ✨ ✨ ✨ ✨ ✨ ✨':^68}",
        f"{'🏁 ✨ ✨ ✨ ✨ ✨ ✨ ✨ 🏆':^68}",
    ]
    
    
    for frame in frames:
        sys.stdout.write('\r' + frame.ljust(20))
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    print()
    print(f"{'🏆  ¡TERMINÓ EL JUEGO!  🏆':^68}")
    print()
    time.sleep(0.8)

def juego():
    print()
    jugadores = inputs("Ingrese Numero de jugadores: ")
    maxPuntos = inputs("Ingrese Maximo de puntos Permitidos: ")
    print()
    i=0
    puntos = 0
    Ronda = 1
    jugadorr = 1
    while True:
        if i % 2 != 0:
            puntos -= 1
            print('-'*68)
            print(f"| {'Ronda: ':^6} {Ronda:^2} | {'Posicion: ':^6} {i:^2} | {'Jugador: ':^6} {jugadorr:^2} |  { 'Resta 1 Puntos: ':^16} {puntos:^2} |")
            print('-'*68)
            animacionImpar()

        else:
            puntos += 2
            print('-'*68)
            print(f"| {'Ronda: ':^6} {Ronda:^2} | {'Posicion: ':^6} {i:^2} |  {'Jugador: ':^6} {jugadorr:^2} | {'Suma 2 Puntos: ':^16} {puntos:^2} |")
            print('-'*68)
            
            animacionPar()
        jugadorr += 1  
        i = i + 1
        if i==jugadores:
            if puntos < maxPuntos:
                i = 0
                Ronda += 1
                print()
            else:
                break
    animacionFin()
    print()
def main():
    while True:
        print("="*68)
        print(f"{'MENU JUEGO':^68}")
        print()
        print(f"{'1. Iniciar':^68}")
        print(f"{'2. Salir  ':^68}")
        print()
        print("="*68)
        print()
        opc = inputs("ingrese Opcion 1 o 2: ")
        if opc == 1 :
            juego()
        elif opc == 2 :
            print('Gracias')
            break
        else:
            print("dato errado solo 1 o 2")
            print("...")
        
main()



    
    
    


    
        