def hash_function(value, num_celdas):
    return value % num_celdas

def store_in_memory(data_array, num_celdas):
    arrayMemoria = [None] * num_celdas  # Inicializamos el array de celdas de memoria
    for value in data_array:
        index = hash_function(value, num_celdas)

        # Colocamos el valor en la posición calculada
        while arrayMemoria[index] != None:
            index = (index + 1) % num_celdas  # Linealmente desplazamos si hay colisión

        arrayMemoria[index] = value

    return arrayMemoria

def main():
    # Solicita el número de celdas para el arreglo
    print("---------- ¡Bienvenido al programa Hashing! ----------")
    while True:
        try:
            num_celdas = int(input("¿Cuántas celdas necesitas para almacenar tus datos? "))
            if num_celdas <= 0:
                print("Por favor, ingresa un número mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    
    # Crear el arreglo y llenarlo con datos ingresados por el usuario
    array = []
    for i in range(num_celdas):
        while True:
            try:
                numero = int(input(f"Ingrese un número entero: "))
                array.append(numero)
                break
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
    
    # Imprimir el resultadoprint("\nLos datos almacenados en el arreglo son:")
    print("\n¡Tu arraglo se creó usando Hashing con éxito!\n", store_in_memory(array, num_celdas))

main()