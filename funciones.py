# Ejemplo de una función simple en Python.

# Para definir una función en Python se usa la palabra reservada "def"

  
def saludar():
  print("Bienvenido")

def saludarNombre(nombreUsuario):
  print(f"Bienvenido {nombreUsuario}")

# Ejemplo de función con retorno 
# Utilizando al estructura de selección (if, elif)

def cruzarSemaforoPeaton(color):
  if color == "rojo":
    return "Puede cruzar la calle"
  elif color == "verde":
    return "No debe cruzar la calle"
  elif color == "amarillo":
    return "Precaución, puede un carro pasar el semáforo"
  else:
    return "Valor desconocido  o incorecto"

def ingresarColorSemaforo():
  colorIngresado = input("Ingrese el color del semáforo: ").lower()
    # Invocar la función cruzarSemaforoPeaton
  print(cruzarSemaforoPeaton(colorIngresado))
    
#Definición de la función Main
if __name__ == "__main__":
  saludar() # Invoca a la primera función saludar
  saludarNombre("Jeferson") # Invocar a la función saludar_nombre

  ingresarColorSemaforo()
  
    