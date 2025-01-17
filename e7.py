
# Función para sumar dos números
def suma(a, b):
    return a + b

# Función principal que pide los números al usuario y muestra el resultado
def main():
    # Pedimos al usuario los dos números
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # Llamamos a la función suma y obtenemos el resultado
    resultado = suma(num1, num2)
    
    # Mostramos el resultado de la suma
    print("La suma de", num1, "y", num2, "es", resultado)

# Llamamos a la función principal
main()
