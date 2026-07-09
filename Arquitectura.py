def ingreso(v):
    x = float(input(f"\nIngrese Valor para {v}"))
    return x

def operacion():
    BM = ingreso("Base Mayor: ")
    bm = ingreso("Base Menor: ")
    am = ingreso("Altura Menor: ")

    AM = (BM/bm)*am

    return BM, bm, am, AM            
            
def tablero(BM, bm, am, AM):    
    print(f"""
*************************************
*                                   *
*      CALCULADORA DE ALTURA        *
*            EDIFICIO               *  
*                                   *
* Base Mayor   = {BM:.2f}              *
* Base Menor   = {bm:.2f}              *
* Altura Menor = {am:.2f}              *
*                                   *
*      {BM:.2f}                        *
*      -------  X {am:.2f} = {AM:.2f}     *  
*      {bm:.2f}                        *
*                                   *
*     AlTURA EDIFICIO = {AM:.2f}       *
*                                   *
*************************************

""")
    
def menu():    
    while True:
        print("""
*************************************
*                                   *
*      CALCULADORA DE ALTURA        *
*            EDIFICIO               *  
*                                   *
*       1. INGRESAR VALORES         *
*       2. SALIR                    *
*                                   *
*************************************
""")
        opc = int(input("Ingrese opcion 1 o 2: "))
        if opc == 1:
            BM, bm, am, AM = operacion()
            tablero(BM, bm, am, AM)
        elif opc == 2:
            print("Gracias por la Confianza")
            break   
          
        else:
            print("Dato Errado")

menu()