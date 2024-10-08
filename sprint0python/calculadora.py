from operaciones import suma, resta, multiplication, division

#Empezamos con un bucle para seguir ejecutando la calculadora hasta que por teclado le mandemos parar posteriormente
while True:
    #Aquí se introducen los valores sobre los que vamos a realizar la operación
    print("Introduce el primer número:")
    n1 = int(input())
    print("Introduce el segundo número:")
    n2 = int(input())

    #Elegimos que operación queremos realizar
    print("Que operación quieres realizar? (1. Suma | 2. Resta | 3. Multiplicar | 4. División")
    option=int(input())

    #Depende de lo que hayamos elegido se realiza una operación u otra, si no es ninguna da mensaje de error
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

    #Muestra por pantalla el resultado de lo que acabamos de calcular
    print(f"El restulado es:", result)

    #Elegimos si realizar otra operación o se finaliza el programa.
    print("Quieres realizar otra operacion?")
    option=input()

    if option == 'n' or option == 'N':
        break