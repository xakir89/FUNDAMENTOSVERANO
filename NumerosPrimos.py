def ingreso():
    x = int(input("ingrese un numero: "))
    return x
def esprimo():
    x = ingreso()
    if x <= 1:
        return False  
    for i in range(2, x):
        if x % i == 0:
            print("No Primo")
            return False
    print("Primo")
    return True

def main():
    while True:
        print("*"*49)
        print(f"|{"OPCIONES":^47}|")
        print("*"*49)
        print(f"|{"1. REVISAR NUMEROS PRIMOS":^47}|")
        print(f"|{"2. SALIR":^47}|")
        print("*"*49)
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            esprimo()
        elif opc == 2:
            print("salir")
            break
        else:
            print("Dato Errado")
main()

