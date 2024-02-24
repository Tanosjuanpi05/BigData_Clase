suma=0

for i in range (5):
    numeros=float(input("ingrese los numeros {} " .format(i+1)))
    suma += numeros
    promedio=suma/5
    
    print(" el promedio es: " ,promedio)