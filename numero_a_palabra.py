def numero_a_palabras(numero):
    """
    Convierte un número entero no negativo (hasta 999) a su representación en palabras en español.
    """
    if not isinstance(numero, int) or numero < 0 or numero > 999:
        return "Número fuera de rango o tipo no válido."

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    diez_a_diecinueve = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if numero == 0:
        return "cero"

    palabras = []

    # Centenas
    if numero >= 100:
        c = numero // 100
        if c == 1 and numero != 100: # Cien vs Ciento algo
            palabras.append("ciento")
        elif c == 1 and numero == 100:
            palabras.append("cien")
        else:
            palabras.append(centenas[c])
        numero %= 100 # Reducir el número a las decenas y unidades

    # Decenas y Unidades
    if numero >= 20:
        d = numero // 10
        u = numero % 10
        palabras.append(decenas[d])
        if u > 0:
            if d == 2: # Caso especial para "veintiuno", "veintidós", etc.
                palabras.append(unidades[u])
            else:
                palabras.append("y")
                palabras.append(unidades[u])
    elif numero >= 10:
        palabras.append(diez_a_diecinueve[numero - 10])
    elif numero > 0: # Unidades
        palabras.append(unidades[numero])

    return " ".join(palabras).strip()

# --- Parte principal del programa ---
if __name__ == "__main__":
    while True:
        try:
            entrada = input("Por favor, ingresa un número entero (0-999) o 'salir' para terminar: ")
            if entrada.lower() == 'salir':
                break
            
            numero_ingresado = int(entrada)
            
            resultado_palabras = numero_a_palabras(numero_ingresado)
            print(f"El número {numero_ingresado} se escribe como: {resultado_palabras.capitalize()}")
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")