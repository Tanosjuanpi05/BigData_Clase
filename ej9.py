def area_rectangulo():
    
    base = float(input("selecciona una base: "))
    altura = float(input("selecciona una altura: "))
 
    area = base * altura
    
    return area

area = area_rectangulo()
print("El área del rectángulo es:", area)
