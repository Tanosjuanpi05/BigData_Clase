def calcular_comision(ventas):
    if ventas > 50000:
        comision = 0.12  
    elif 30000 <= ventas <= 50000:
        comision = 0.08  
    elif 8000 <= ventas <= 29999:
        comision = 0.05  
    else:
        comision = 0 

    comision_a_pagar = ventas * comision
    return comision_a_pagar

ventas = float(input("ventas mensuales: "))

comision_pagar = calcular_comision(ventas)

print("la comision es: {:.2f} pesos".format(comision_pagar))
