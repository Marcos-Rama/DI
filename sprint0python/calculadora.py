from operaciones import suma, resta, multiplication, division


while True:
    print("Introduce el primer número:")
    n1 = int(input())
    print("Introduce el segundo número:")
    n2 = int(input())


    print("Que operación quieres realizar? (1. Suma | 2. Resta | 3. Multiplicar | 4. División")
    option=int(input())

    if option == 1:
        result = suma(n1,n2)
    elif option == 2:
        result =resta(n1,n2)
    elif option == 3:
        result =multiplication(n1,n2)
    elif option == 4:
        result =division(n1,n2)
    else:
        result =print("Operacion erronea")

    print(f"El restulado es:")

    print("Quieres realizar otra operacion?")
    option=input()


    if option == 'n' or option == 'N':
        break