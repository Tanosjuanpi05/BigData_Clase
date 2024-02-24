
def sobres(cantidad_sobres):
    tarifa_base=0.80
    limite_sobres_base=50
    tarifa_extra=1.00

    if cantidad_sobres<=limite_sobres_base:
        pago_total=cantidad_sobres*tarifa_base
    else:
        sobres_base=limite_sobres_base
        sobres_extra=cantidad_sobres-limite_sobres_base
        pago_total=(sobres_base*tarifa_base)+(sobres_extra*tarifa_extra)

    return pago_total

sobres_entregados=int(input("Ingrese la cantidad de sobres entregados: "))

pago_total=sobres(sobres_entregados)
print(f"El pago total por {sobres_entregados} sobres entregados es: ${pago_total:.2f}")
