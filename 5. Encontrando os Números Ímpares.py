def numeros_impares(lista):
    return [n for n in lista if isinstance(n, int) and n % 2 != 0]
numeros = [987654321,2,7654321,56,1234567,1,88888,3,42,999999,5,1000000000,13,101010,7,444,9,2,13,9]
print(numeros_impares(numeros))
