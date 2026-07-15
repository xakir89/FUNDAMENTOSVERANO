
n,m,a = map(int,input().split( ))
ancho, alto = (n + a -1)//a, (m + a -1)//a 
print(id(ancho))
print(ancho*alto)