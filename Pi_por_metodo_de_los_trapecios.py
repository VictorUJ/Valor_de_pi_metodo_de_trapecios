n = 10 #numero de trapecios que se desean para dividir el circulo
suma = 0
i = 0
while i < n:
    parte1 = (pow(1 - pow((i)/n,2),0.5) + pow(1 - pow((i+1)/n,2),0.5))/(2*n)
    suma += parte1
    i = i + 1
    pass
print("La suma del area es: ", suma)
pi = 4*suma
print("El valor de PI con n =", n, " es: ", pi)