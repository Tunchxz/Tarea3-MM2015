def generar_numeros_pseudoaleatorios(m, a, c, s, n):
    numeros_pseudoaleatorios = []
    x = s  # x0 = s
    for _ in range(n):
        x = (a * x + c) % m  # Fórmula recursiva para xn
        numeros_pseudoaleatorios.append(x)
    return numeros_pseudoaleatorios

def obtener_entrada_valida(mensaje, tipo, condicion):
    while True:
        try:
            valor = tipo(input(mensaje))
            if not condicion(valor):
                print("Entrada fuera de los límites permitidos. Por favor, ingrese un valor válido.")
            else:
                return valor
        except ValueError:
            print(f"Entrada inválida. Por favor, ingrese un valor {tipo.__name__} válido.")

def interfaz_usuario():
    print("Bienvenido al Generador de Números Pseudoaleatorios")
    
    m = obtener_entrada_valida("\nIngrese el valor para el módulo m (mayor que 2): ", int, lambda x: x > 2)
    a = obtener_entrada_valida(f"\nIngrese el valor para el multiplicador a (2 ≤ a < {m}): ", int, lambda x: 2 <= x < m)
    c = obtener_entrada_valida(f"\nIngrese el valor para el incremento c (0 ≤ c < {m}): ", int, lambda x: 0 <= x < m)
    s = obtener_entrada_valida(f"\nIngrese el valor para la semilla s (0 ≤ s < {m}): ", int, lambda x: 0 <= x < m)
    n = obtener_entrada_valida("\nIngrese la cantidad de números a generar n (positivo): ", int, lambda x: x > 0)

    resultado = generar_numeros_pseudoaleatorios(m, a, c, s, n)
    print("\nLos números pseudoaleatorios generados son:")
    print(resultado)

# Ejecutar la interfaz de usuario en consola
interfaz_usuario()
