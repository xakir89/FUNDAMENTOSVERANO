def ingrese(v):
    x = int(input(f"ingrese Valor para {v}"))
    while x <  0:
        print("los lados del figura deben ser positivos: ")
        x = int(input(f"ingrese Valor para {v}"))
    return x
def trapesio():
    bma = ingrese(f"""

                **********
               *          *          
              *            *         
             *              *
            ******************                   
            |-- Base Mayor ---| 

Base Mayor: """)
    bme = ingrese(f"""
                          
               |-Ba Menor-|          
                **********
               *          *          
              *            *         
             *              *
            ******************
                  
Base Menor: """)
    while bma <= bme:
        print("base menor no puede ser igual o mas grande que la base mayor")
        bme = ingrese(f"""
                          
               |-Ba Menor-|          
                **********
               *          *          
              *            *         
             *              *
            ******************
Base Menor: """) 


    a = ingrese(f"""
                      
      --------- **********
      |        *          *          
    Altura    *            *         
      |      *              *
      ----- ******************                  

Altura: """)
    area = ((bma+bme)*a)/2
    return area, bma, bme, a

def main():
    while True:
        
        print("""
************ BIENVENIDO AL ALGORITMO DE AREAS ************
*                                                        *
*                1. hallar Area Trapesio                 *
*                2. Salir                                *    
*                                                        *
**********************************************************
""")
        opc = int(input("ingrese 1 o 2 para opciones: "))
        if opc == 1:
            area, bma, bme, a = trapesio()
            print(f"""
**********************************************************
*                                                        *                  
*                    AREA DEL TRAPESIO                   *
*                                                        *
*             |-Ba Menor-|                               *
*    --------- **********                                *
*    |        *          *                               *
*  Altura    *            *                              *       
*    |      *              *                             *
*    ----- ******************                            *
*          |-- Base Mayor ---|                           * 
*                                                        *
*     ({bma:.1f} + {bme:.1f}) X {a}                               *
*   ------------------------       = {area:.2f}              *
*               2                                        *
*                                                        *
**********************************************************
""")
        elif opc == 2:
            print("gracias por sus contar con nuestros servicios.")
            break
        else:
            print("dato errado solo 1 o 2.")

main()
