def numeros_pares(inicio, fin):
   
    inicio += 1 if inicio % 2 != 0 else 0
    fin -= 1 if fin % 2 != 0 else 0
    
    for numero in range(inicio, fin + 1, 2):
        print(numero)

inicio = int(input("inicio del rango: "))
fin = int(input("fin del rango: "))

numeros_pares(inicio,fin)
