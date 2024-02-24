def calcular_monto(monto_compra, metodo_pago):
    if metodo_pago == "efectivo":
        descuento = 0.20  
    elif metodo_pago == "tarjeta":
        descuento = 0.10  
    else:
        descuento = 0  
    
    monto_descuento = monto_compra * descuento
    monto_a_pagar = monto_compra - monto_descuento
    
    return monto_a_pagar

monto_compra = float(input("ingresa el monto: "))
metodo_pago = input("selecciona un metodo de pago (efectivo o tarjeta): ").lower()

monto_con_descuento = calcular_monto(monto_compra, metodo_pago)

print("el monto final es: {:.2f} pesos".format(monto_con_descuento))
