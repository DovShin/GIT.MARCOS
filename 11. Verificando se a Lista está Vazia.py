def lista_vazia(lista):
    return len(lista) == 0

opcao = input("Digite '1' para testar uma lista vazia ou '2' para testar uma lista com elementos: ")

if opcao == "1":
    lista_teste = []
elif opcao == "2":
    lista_teste = [1, 2, 3]  
else:
    print("Opção inválida.")
    lista_teste = []

print(lista_vazia(lista_teste))
