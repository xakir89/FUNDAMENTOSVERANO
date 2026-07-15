
while True:
    w = int(input("Ingrese el peso de la Sandia: "))
    if 1 <= w <= 100:
        if w % 2 == 0:
            x = w / 2
            print(f"Es par y se puede dividir {x}\n")
            break
            
        else:
            print("Es Impar no se puede dividir a la mitad\n")
            break
    else:
        print("El peso de la sandia debe estar entre 1 y 100\n")
        

