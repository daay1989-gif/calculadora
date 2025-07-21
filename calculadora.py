# calculadora_final.py

def sumar(a, b):
    """Realiza la operación de suma."""
    return a + b

def restar(a, b):
    """Realiza la operación de resta."""
    return a - b

def multiplicar(a, b):
    """Realiza la operación de multiplicación."""
    return a * b

def dividir(a, b):
    """Realiza la operación de división, manejando la división por cero."""
    if b == 0:
        return "Error: ¡No se puede dividir por cero!"
    return a / b

def main():
    """Función principal de la calculadora."""
    print("--- Calculadora Básica ---")
    print("Selecciona una operación:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

    while True:
        eleccion = input("Ingresa tu elección (1/2/3/4/5): ")

        if eleccion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresa números.")
                continue

            if eleccion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif eleccion == '2':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif eleccion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif eleccion == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        elif eleccion == '5':
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()