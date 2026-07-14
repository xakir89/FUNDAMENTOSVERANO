coste_original = 20000
vida_util = 6
valor_recuperacion = 2000
anio = 2026

for i in range(1,vida_util + 1  ):
    d = (coste_original - valor_recuperacion)/i
    print(f"Fila | Año  | Depreciación | Depreciación Acumulada | Valor Anual ")
    print()
    print(f" {i}   | {anio} |     2000      |        {valor_recuperacion}          |    {d}")
    print()
    coste_original = d
    valor_recuperacion += 2000
    
    
    anio += 1
    

