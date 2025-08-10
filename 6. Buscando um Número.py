def buscar_numero(valor, lista):
    return valor in lista
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


try:
    valor_digitado = int(input("Digite um número para verificar se está na lista: "))
    resultado = buscar_numero(valor_digitado, numeros)
    print(resultado)
except ValueError:
    print("Por favor, digite apenas números inteiros.")
