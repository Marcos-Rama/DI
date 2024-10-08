
#Esta clase establecerá una serie de operaciones aritméticas básicas.

def suma(n1,n2):
    """
    Esta operación realiza una suma de los dos valores que se envíen como parámetro

    Parámetros

    n1 (int): Primer valor de la operación
    n2 (int): Segundo valor de la operación

    Retorna:
    int: la suma de n1 y n2

    """
    return n1 + n2

def resta(n1, n2):
    """
    Esta operación realiza una resta de los dos valores que se envíen como parámetro

    Parámetros

    n1 (int): Primer valor de la operación
    n2 (int): Segundo valor de la operación

    Retorna:
    int: la resta de n1 y n2

    """
    return n1 - n2

def multiplication(n1, n2):
    """
    Esta operación realiza una multiplicación de los dos valores que se envíen como parámetro

    Parámetros

    n1 (int): Primer valor de la operación
    n2 (int): Segundo valor de la operación

    Retorna:
    int: la multiplicación de n1 y n2

    """
    return n1*n2

def division(n1,n2):
    """
    Esta operación realiza una división de los dos valores que se envíen como parámetro

    Parámetros

    n1 (int): Primer valor de la operación
    n2 (int): Segundo valor de la operación

    Retorna:
    int: la división de n1 y n2

    """
    if n2 == 0:
        print("No se puede dividir por 0")
    else:
        return n1/n2

#Ejemplos para comprobar que funcionan

print(f"Resultado: ",suma(9,2))
print(f"Resultado: ",resta(9,2))
print(f"Resultado: ",multiplication(9,2))
print(f"Resultado: ",division(9,2))