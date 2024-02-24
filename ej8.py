import random


numero_aleatorio = random.randint(1, 20)
intentos = 0
while True:
    intento = int(input("adivina el numero (entre 1 y 20): "))
    intentos += 1

    if intento == numero_aleatorio:
        print("adivinaste el numero {} intentos.".format(intentos))
        break
    elif intento < numero_aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor.")
