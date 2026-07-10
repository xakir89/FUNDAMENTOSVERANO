def operaciones():
    compuertas = ['A','P','R','A','P','R']
    e0 = float(input("Eneria inicial en Joules (J): "))
    Eimp = float(input("Energia de impulso: "))
    Efreno = float(input("Energia de Freno: "))

    particula_viva = True
    compuerta_actual = 0
    Energia_actual = e0

    while compuerta_actual < len(compuertas) and particula_viva:
        tipo = compuertas[compuerta_actual]
        compuerta_actual = compuerta_actual + 1
        

        print(f"\n[Compuerta #{compuerta_actual} - {tipo}]")
        print(f"\n> ENERGIA AL ENTRAR: {Energia_actual:.2f}")
        
        if tipo =='A':      
    # COMPUERTA TIPO A (ACELERADORA)
            if 0 < Energia_actual < 15:
                Energia_actual = Energia_actual+(Eimp * 0.5)
                print(f"Perdida de Eficiencia del 50% {Energia_actual:.2f}")
            elif e0 > 15:
                Energia_actual = Energia_actual + Eimp
                print(f"Incrementa la Energia de la Particula {Energia_actual:.2f}")
            else:
                print("La particula no tiene energia o es igual a 0, para completamente")
                particula_viva = False
                
    # COMPUERTA TIPO P (PASIVA / FRENO)
        elif tipo == 'P':
            Energia_actual = Energia_actual - Efreno
            print(f"Enerigia atual menos la Energia de Freno: {Energia_actual:.2f}")
            if 1.0 <= Energia_actual <= 5.0:
                print("Zona de Resonancia Destructiva no se puede avanzar particula atrapada en el intervalo (1.0 a 5.0)")
                particula_viva = False            
    # COMPUERTA TIPO R (RESONANTE)
        elif tipo == 'R':
            if int(Energia_actual) % 2 == 0:
                Energia_actual = Energia_actual * 1.2
                print(f"factor de Amplificacion: {Energia_actual:.2f}")
            else:
                Energia_actual = Energia_actual - 5.0
                print(f"Penalizacion - 5.0 J: {Energia_actual:.2f}")

def menu():
    while True:
        print("""
*******************************************
*   Simulador de Filtrado de Partículas   *
*    en Acelerador Magnético Secuencial   *
*                                         *
*    1. ingresar valores solicitadios     *             
*    2. Salir                             *
*                                         *
*******************************************
              """)      
        opc = int(input("Ingrese Opcion: "))
        if opc == 1:
            operaciones()
        elif opc == 2:
            print("""
Gracias por confiar en nuestros servicios
    Contactanos y solicita tu software
        Whatsapp: 301 553 0836
                  """)
            break
        else:
            print("Dato errado solo puede ser 1 o 2")
menu()