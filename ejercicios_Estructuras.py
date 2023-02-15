# Ejercicio 1 Uso de if/else en python.

def evaluacionEmpleado ():
  
  puntuacion = float(input("Por favor digite la puntuación del empleado,\n según corresponda a: 0.0 , 0.4, 0.6 o superior: "))
  
  dinero = 2400

  if puntuacion == 0.0:
    nivel = "Inaceptable"
    print(f"\nSu condición es {nivel} y su dinero es {dinero * puntuacion} euros\n")
  elif puntuacion == 0.4:
    nivel = "Aceptable"
    print(f"\nSu condición es {nivel} y su dinero es {dinero * puntuacion} euros\n")
  elif puntuacion >= 0.6:
    nivel = "Meritorio"
    #dinero =
    print(f"\nSu condición es {nivel} y su dinero es {dinero * puntuacion} euros\n")
  else:
    print("\nLa el valor digitado es incorrecto o es un numero intermedio de 0.0 a 0.6")


# Ejercicio 2 uso de For

def solicitarPalabra():
  palabra = input("Ingresa una palabra: \n")
  for i in range(1, 11):
    print(f"\nposición: {i} \n")
    print(f" {palabra}")

# Ejercico 3 uso de For 

def calcularDivisibles():
  cantidad = 0
  for i in range (0, 3501):
    if i % 7 == 0:
      cantidad += 1
  print(f"La cantidad de numeros divisibles entre 7 es de: {cantidad}")

'''Miércoles 15 de Febrero'''

# Ejercicio 1

def tablaMultiplicar():
  numero = int(input("Digite un numero para obtener su tabla de multiplicar: \n"))

  for i in range (1, 11):
    print(f"\n {numero} x {i} es: {numero * i} \n")

# Ejercicio 2

def areaCirculo(r):
  
  PI = 3.14
  return PI * (r**2)

def volumenCilindro():
  h = float(input("Digite la altura del cilindro: \n"))
  radio = float(input("Digite el radio del cilindro: \n"))
  area = areaCirculo(radio)
  print(f"El volumen del cilíndro es: {area * h}: ")

# Ejercicio 5

def cuentaAtras():
  numero = int(input("Digite un numero entero positivo: ")) 
  # Le asigno el valor del numero al contador  
  i = numero
  while i > 0: # Evaluo que el numero sea positivo
    i -= 1 # Decremento del numero
    print(i, ",", end=" ")

# Ejercicio 6

def solicitarEdad():
  edad = int(input("Digite su edad: \n"))
  i = 0
  while i < edad:
    i +=1
    print(i, end=" ")



  
if __name__ == "__main__":
  #evaluacionEmpleado()
  #solicitarPalabra()
  #calcularDivisibles()
  #tablaMultiplicar()
  #area_circulo = f"El area del círculo equivale a {areaCirculo(12)}"
  #print(area_circulo)
  #volumenCilindro()
  #cuentaAtras()
  solicitarEdad()
