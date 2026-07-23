def inputs(s):    
    print("="*68)
    print()
    print(f"{'HELADERIA DON PEPE':^68}")
    print()
    print(f"{'1. Helado Chocolate':^68}")
    print(f"{'2. Helado Vainilla ':^68}")
    print(f"{'2. Salir           ':^68}")
    print()
    print("="*68)
    print()
    try:
        opc = int(input(s)) 
        print("...")
    except ValueError:
        print(f"Error entrada no valida solo puede ingresar números")
        print("...")
    return opc



        
def main():
    entrada = inputs('escoje una opcion: ')
    if entrada == 1:
        print('Helado CHocolate')
        print('$ 3')        
        main()
    elif entrada == 2:
        print('Helado Vainilla')
        print('$ 2')
        main()
    elif entrada == 3:
        print('saliendo')
    else:
        print('dato errado solo hay 3 opciones')
        main()
    return entrada

main()

