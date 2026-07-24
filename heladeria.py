def entradas(s):
    opc = None    
    try:
        opc = int(input(s))
    except ValueError:
        print(f"Error entrada no valida solo puede ingresar números\n...")
    return opc
def confirmar(conChoco,conVaini):
    print("="*68,'\n')
    print(f"{'DESEAS OTRO HELADO':^68}")
    print(f"{'1. SI ':^68}")
    print(f"{'2. NO ':^68}",'\n')
    print("="*68,'\n')
    opc = entradas("Deseas otro helado: ")
    if opc == 1:
        return main(conChoco,conVaini)
    elif opc == 2:
        return resumen(conChoco,conVaini)
    else:
        print('Dato Errado solo 1 o 2\n...')
        return confirmar(conChoco,conVaini)
def resumen(conChoco,conVaini):
        precioChoco = 3
        precioVaini = 2
        print("="*68,'\n')
        print(f"{'RESUMEN COMPRA':^68}"'\n')
        print(f"{'DESCRIOCION':^30} {'CANTIDAD':^10} {'VALOR U':^10} {'TOTAL':^10}\n")
        print(f"{'1. Total Chocolate: ':^30} {conChoco:^10} {precioChoco:^10} {'$':^5}{conChoco*precioChoco:^5}")
        print(f"{'2. Total Vainilla: ':^30} {conVaini:^10} {precioVaini:^10} {'$':^5}{conVaini*precioVaini:^5}\n")
        print("="*68,'\n')
        print('saliendo\n...')
def main(conChoco = 0, conVaini = 0):
    print("="*68,'\n')
    print(f"{'HELADERIA DON PEPE':^68}",'\n')
    print(f"{'1. Helado Chocolate':^68}")
    print(f"{'2. Helado Vainilla ':^68}")
    print(f"{'3. Salir           ':^68}",'\n')
    print("="*68,'\n')
    entrada = entradas('escoje una opcion: ')
    if entrada == 1:
        print('Helado CHocolate\n$ 3\n...')
        return confirmar(conChoco + 1, conVaini)
    elif entrada == 2:
        print('Helado Vainilla\n$ 2\n...')
        return confirmar(conChoco, conVaini + 1)
    elif entrada == 3:
        return resumen(conChoco,conVaini)
    else:
        print('dato errado solo hay 3 opciones')
        return main(conChoco, conVaini)

main()

