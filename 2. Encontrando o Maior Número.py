def maior_numero(lista):
    if not lista:
        return None
    return max(lista)
numeros = [987654321,2,7654321,56,1234567,1,88888,3,42,999999,5,1000000000,13,101010,7,444,9,2,13,9]
print(maior_numero(numeros))
