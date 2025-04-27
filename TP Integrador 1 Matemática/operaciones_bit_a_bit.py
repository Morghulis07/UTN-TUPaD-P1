
# Realiza la operación AND bit a bit entre dos arrays 
def operacion_and(arr1, arr2):
    index = len(arr1)
    res = []
    for i in range(index):
        res.append(arr1[i] and arr2[i])
    return res

# Realiza la operación OR bit a bit entre dos arrays 
def operacion_or(arr1, arr2):
    index = len(arr1)
    res = []
    for i in range(index):
        res.append(arr1[i] or arr2[i])
    return res

# Realiza la operación NOT bit a bit de un array
def operacion_not(arr):
    index = len(arr)
    res = []
    for i in range(index):
        res.append(abs(arr[i] - 1))
    return res

# Realiza la operación XOR bit a bit entre dos arrays 
def operacion_xor(arr1, arr2):
    # !(a and b) and (a or b)
    return operacion_and(operacion_not(operacion_and(arr1, arr2)), operacion_or(arr1, arr2))

# Devuelve la representación binaria de un numero en un array que contiene 0s y 1s
# Se utiliza la técnica de los restos en la división sucesiva por 2
def bit_array(num):
    array = []
    while num > 0:
        array.append(num % 2)
        num //= 2
    array.reverse()
    return array

# Rellena con tantos ceros en el inicio como haga falta para que tenga la longitud especificada
def rellenar_con_ceros(arr, lng):
    while len(arr) < lng:
        arr.insert(0, 0)


# Convierte un array de bits a su represenctión en base 10
def bits_a_decimal(arr):
    length = len(arr)
    res = 0
    for i in range(length):
        res = res + arr[i] * pow(2, length - i - 1)
    return res

def realizar_operaciones(n1, n2):
    arr1 = bit_array(n1)
    arr2 = bit_array(n2)

    max_len = max(len(arr1), len(arr2))

    rellenar_con_ceros(arr1, max_len)
    rellenar_con_ceros(arr2, max_len)

    res_and = operacion_and(arr1, arr2)
    res_or = operacion_or(arr1, arr2)
    res_xor = operacion_xor(arr1, arr2)
    print()
    print(f"Número 1: {arr1}")
    print(f"Número 2: {arr2}")
    print()
    print(f"{arr1} AND {arr2} = {res_and} = {bits_a_decimal(res_and)}")
    print(f"{arr1} OR  {arr2} = {res_or} = {bits_a_decimal(res_or)}")
    print(f"{arr1} XOR {arr2} = {res_xor} = {bits_a_decimal(res_xor)}")


def obtener_numero_positivo(posicion): 
    num = int(input(f"Ingrese el {posicion} número: "))  
    while num <= 0:
        print("El número debe set positivo.")
        num = int(input(f"Intente nuevamente. Ingrese el {posicion} numero: "))
    return num

num1 = obtener_numero_positivo("primer")
num2 = obtener_numero_positivo("segundo")

realizar_operaciones(num1, num2)
