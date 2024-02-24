#Ejercicio 1 Juan Pablo Tanos Batarse 


def bonos(antiguedad):
    sueldo_base=7000

    if antiguedad>3:
        bono=500
    else:
        bono=100

    sueldo_total=sueldo_base+bono
    return sueldo_total

años_de_trabajo=int(input("Que antiguedad tiene el empleado?: "))

sueldo_con_bono=bonos(años_de_trabajo)
print(f"el sueldo del empleado con {años_de_trabajo} años de antiguedad es: {sueldo_con_bono}.")
