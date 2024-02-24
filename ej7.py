while True:
    try:
        numero = int(input("numero del 1 al 10: "))
        if 1 <= numero <= 10:
            break  
        else:
            print("ingresaste un numero que no esta en rango.")
    except ValueError:
        print("ingresa un numero valido.")

print("numero valido:", numero)
