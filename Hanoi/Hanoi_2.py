class Hanoi:
  def __init__(self, numero):
    self.num = numero
    print(f"Creando Hanoi para: {self.num} Fichas")

  def hanoi(self, num, desde, aux, hasta):

    if num == 1:
      print(f"Pase la Ficha {num} a la Torre {hasta}")
      return
    Hanoi.hanoi(self, num=num-1, desde=desde, aux=hasta, hasta=aux)
    print(f"Pase la Ficha {num} a la Torre {hasta}")
    Hanoi.hanoi(self, num=num-1, desde=aux, aux=desde, hasta=hasta)
      

try:
  valor = int(input("Ingrese un numero: "))
  mi_hanoi = Hanoi(valor)
  mi_hanoi.hanoi(mi_hanoi.num, "A", "B", "C")
except Exception as e:
  print("ERROR:", e, "¡¡¡Debe ingresar un número!!!")
  print("Debe ingresar un número")
finally:
  print("")



