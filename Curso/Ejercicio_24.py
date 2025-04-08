#Ejemplo para break

print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)

print("Fin del prgrama, la sentencia break se ha ejecutado.")

#Ejemplo para continue

print("\nwhile con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)
