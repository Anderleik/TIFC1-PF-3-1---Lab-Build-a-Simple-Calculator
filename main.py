# CALCULADORA SENCILLA
try:
    # Ingresamos los dos numeros
    num1 = int(input())
    num2 = int(input())
    
    # Sumamos los dos numeros ingresados e imprime el resultado
    print(num1 + num2)

    # CALCULADORA AVANZADA
    print("\n" + "="*30)
    print("  MODO CALCULADORA AVANZADA")
    print("="*30)
    # Usamos while True para que el programa siga corriendo hasta que decidamos salir.
    while True:
        # Mostramos las operaciones que podemos realizar
        print("\nQue operacion deseas realizar ahora?")
        print("1. Restar (A - B)")
        print("2. Multiplicar (A * B)")
        print("3. Dividir (A / B)")
        print("4. Modulo / Residuo (A % B)")
        print("5. Sumar 3 numeros (A + B + C)")
        print("6. Operacion mixta libre (ej. 2 + 4 - 3)")
        print("7. Salir")
        # Creamos la variable opcion.
        opcion = input("\nElige una opcion (1-7): ")
        # Condicion para salir del programa.
        if opcion == '7':
            print("Saliendo...")
            break
        # Condicion para realizar las operaciones del menu con la lista 1, 2, 3, 4.
        if opcion in ['1', '2', '3', '4']:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))
            
            if opcion == '1':
                print("Resultado:", a - b)
            elif opcion == '2':
                print("Resultado:", a * b)
            elif opcion == '3':
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Error: No se puede dividir entre cero")
            elif opcion == '4':
                print("Resultado:", a % b)

        # Condicion para realizar la suma de 3 numeros.        
        elif opcion == '5':
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))
            c = int(input("Ingresa el tercer numero: "))
            print("Resultado:", a + b + c)

        # Condicion para realizar una operacion mixta libre.    
        elif opcion == '6':
            expresion = input("Escribe la ecuacion: ")
            print("Resultado:", eval(expresion))

        # Condicion para cuando el usuario ingresa una opcion no valida.
        else:
            print("Opcion no valida.")

# Evita que el codigo se cierre si el usuario ingresa un EOF (Ctrl+D o Ctrl+Z) en la entrada.
except EOFError:
    pass