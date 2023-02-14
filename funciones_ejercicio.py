# Immplemente las siguientes funciones

# Primer función a implementar
# Función determinaEstadoNumero, esta función recibe un número, y determina si el número es positivo, negativo o cero.

def determinaEstadoNumero(numero):
  
  if numero > 0:
    print(f"\nEl número {numero} es positivo")
  elif numero < 0:
    print(f"\nEl número {numero} es negativo")
  elif numero == 0:
    print("\nEl número es cero")
  

# determinaEstadoNumero(23)

# Segunda función a implementar
# Función solicitaNumero un número al usuario y determina el estado del número.

def solicitaNumero():
  numero = int(input("\nIngrese un número para saber si es positivo, negativo o cero: "))
  determinaEstadoNumero(numero)

  
if __name__ == "__main__": 
  solicitaNumero()