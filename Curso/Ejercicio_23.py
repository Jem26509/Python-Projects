num_uno, num_dos = 0, 1
while num_dos <= 200000:
    print(num_uno, num_dos, end=" ")
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos
