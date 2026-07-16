def limite(datoinicial):
    a = 0
    b = 1
    print(a)
    while b <= datoinicial:
        print (b)
        c = a
        a = b
        b = c + b
limite(50)