# Función con ejemplo del uso de for


'''
La función range()
range(inicio, fin, paso/incremento/decremento)
'''

# Mostrar los numeros del 1 al 5
def ejemploUnoUsoFor():
  for i in range(1, 6):
    print(i)

# Mostrar la lista de números siguiente
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

def ejemploDosUsuoFor():
  for i in range (10, 21):
    print(i)

# Mostrar la siguiente lista de números
# 5, 10, 15, 20, 25, 30

def ejemploTresUsoFor():
  for i in range(5, 31, 5):
    print(i)

# Mostrar la lista de números siguiente
# 5, 4, 3, 2, 1

def ejemploCuatroUsoFor():
  for i in range(5, 0, -1):
    print(i)
    
# Definir función main
if __name__ == "__main__":
  print("Lista del 1 al 5")
  ejemploUnoUsoFor()
  print("\n")
  print("Lista del 1 al 20")
  ejemploDosUsuoFor()
  print("\n")
  print("Lista de 5 en 5 hasta 30")
  ejemploTresUsoFor()
  print("\n")
  print("Lista del 5 al 1 decrementando")
  ejemploCuatroUsoFor()