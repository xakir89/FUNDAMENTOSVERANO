coste_original = 20000
vida_util = 6
valor_recuperacion = 2000
depreciacion_acumulada = 0
anio = 2026
d = (coste_original - valor_recuperacion) / vida_util
print()
print(f"Fila | Año  | Depreciación | Depreciación Acumulada | Valor Anual ")
print()
for i in range(1,vida_util+1):
    depreciacion_acumulada += d
    valor_anual = coste_original - depreciacion_acumulada
    print(f" {i}   | {anio} |   {d}    |         {depreciacion_acumulada}          |    {valor_anual}")
    print() 
    anio += 1
    

