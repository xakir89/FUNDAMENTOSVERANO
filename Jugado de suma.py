import sys
import time
def animacionPar():
    print()
    #doble barra \ para que Python imprima una sola \
    frames = [
        "🤾🏼‍♀️🏈         🏃🏻",
        "🤾🏼‍♀️  🏈       🏃🏻",
        "🤾🏼‍♀️    🏈     🏃🏻",
        "🤾🏼‍♀️      🏈   🏃🏻",
        "🤾🏼‍♀️        🏈 🏃🏻",
        "🤾🏼‍♀️         🏈🏃🏻",
    ]

    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.2)    # Pausa de 0.2 segundos por fotograma
    print()
    print()

def animacionImpar():
    #doble barra \ para que Python imprima una sola \
    print()
    frames = [
        "🤾🏼‍♀️         🏈🏃🏻",
        "🤾🏼‍♀️        🏈 🏃🏻",
        "🤾🏼‍♀️      🏈   🏃🏻",
        "🤾🏼‍♀️    🏈     🏃🏻",
        "🤾🏼‍♀️  🏈       🏃🏻",
        "🤾🏼‍♀️🏈         🏃🏻",
    ]

    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.2)    # Pausa de 0.2 segundos por fotograma
    print()
    print()

def animacionFin():
    print()
    frames = [
        "🏁",
        "🏁 ✨",
        "🏁 ✨ ✨",
        "🏁 ✨ ✨ ✨",
        "🏁 ✨ ✨ ✨ 🏆",
    ]
    for frame in frames:
        sys.stdout.write('\r' + frame.ljust(20))
        sys.stdout.flush()
        time.sleep(0.2)
    print()
    print("🏆  ¡TERMINÓ EL JUEGO!  🏆")
    print()

def juego():
    print()
    jugadores = int(input("Ingrese Numero de jugadores: "))
    maxPuntos = int(input("Ingrese Maximo de puntos Permitidos: "))
    print()
    i=0
    puntos = 0
    Ronda = 1

    while True:
        if i % 2 != 0:
            puntos -= 1
            print('-'*51)
            print(f"| {'Ronda: ':^6} {Ronda:^2} | {'Jugador: ':^6} {i:^2} | { 'Resta 1 Puntos: ':^16} {puntos:^2} |")
            print('-'*51)
            animacionImpar()

        else:
            puntos += 2
            print('-'*51)
            print(f"| {'Ronda: ':^6} {Ronda:^2} | {'Jugador: ':^6} {i:^2} | {'Suma 2 Puntos: ':^16} {puntos:^2} |")
            print('-'*51)
            
            animacionPar()
            
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
        print("="*50)
        print(f"{'MENU JUEGO':^50}")
        print()
        print(f"{'1. Iniciar':^50}")
        print(f"{'2. Salir  ':^50}")
        print()
        print("="*50)
        print()
           
        try:
            opc = int(input("ingrese Opcion 1 o 2: ")) 
            print("...")
            if opc == 1 :
                juego()
            elif opc == 2 :
                print('Gracias')
                break
            else:
                print("dato errado solo 1 o 2")
                print("...")
        except ValueError:
            print(f"Error entrada no valida solo puede ingresar números")
            print("...")
main()



    
    
    


    
        