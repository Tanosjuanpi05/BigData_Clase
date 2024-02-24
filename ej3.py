def descuentos(total):
    if total < 500:
        descuento = 0.05  
    elif 500 <= total <= 1500:
        descuento = 0.10  
    else:
        descuento = 0.15  

    descuento_aplicado = total * descuento
    total_a_pagar = total - descuento_aplicado

    return total_a_pagar

total = float(input("Ingrese el monto total de la compra en pesos: "))

total_con_descuento = descuentos(total)

print("El total a pagar con descuento es: {:.2f} pesos".format(total_con_descuento))
