def calcularPorcentajeMasa(masaSoluto, masaDisolucion):
    if masaDisolucion > 0 and masaSoluto > 0:
        porcentaje = (masaSoluto/masaDisolucion)*100
        return porcentaje
    else:
        print("los valores deben ser mayores a 0")
print(calcularPorcentajeMasa(3,9))

def calcularPorcentajeVolumen(volumenSoluto,volTotal):
    if volumenSoluto > 0 and volTotal >0:
        Proporcion = (volumenSoluto/volTotal)*100
        return Proporcion
    else:
        print("los valores no pueden ser negativos ")
print(calcularPorcentajeVolumen(3,3))

def calcularConcentracionFinal(c1,v1,v2):
    if c1 > 0 and v1 >0 and v2 >0:
        nuevaConcentracion = (c1*v1)/v2
        return nuevaConcentracion
    else:
        print("Dato errado mayor a 0")

print(calcularConcentracionFinal(2,-3,4))

def calcularPpm(masMiligramos,VolumenLitros):
    if masMiligramos>0 and VolumenLitros>0:

        concentracion = masMiligramos/VolumenLitros
        return concentracion
    else:
        print("el datop debe ser mayor a 0")
print(calcularPpm(8,9))

def calcularPresionBoyle(p1,v1,v2):
    if p1 > 0 and v1 > 0 and v2 > 0:
        NuevaPresion = (p1*v1)/v2
        return NuevaPresion
    else:
        print("el dato debe ser mayor a 0")

print(calcularPresionBoyle(4,4,2))

def calcularVolumenCharles(v1, t1,t2):
    if v1 > 0 and t2 >0 and t1 > 0:
        nuevoVol= (v1*t2)/t1
        return nuevoVol
    else:
        print("el dato debe ser mayor de 0")
print(calcularVolumenCharles(7, 3, 4))

def calcularPresionGayLussac(p1, t1, t2):
    if p1 >0 and t1 >0 and t2>0:
        presionFinal = (p1*t2)/t1
        return presionFinal
    else:
        print("datos errado")
print(calcularPresionGayLussac(2,3,4))

def calcularDesida(gt,lf):
    if gt >0 and lf >0:
        densidad = gt/lf
        return densidad
    else:
        print("dato errado")
print(calcularDesida(5,6))

def calcularNormalidad(equivalentes,vollitros):
    if equivalentes > 0 and vollitros > 0:
        poderRelativo = equivalentes/vollitros
        return poderRelativo
    else:
        return "dato errado"

print( calcularNormalidad(-32,20))

def calcularVelocidad(cambioConen,tiempoSe):
    if cambioConen> 0 and tiempoSe>0:
        veloconsu = cambioConen / tiempoSe
        return veloconsu
    return "Dato Errado"
print(calcularVelocidad(-3,3))