def extrair_nomes(objetos):
   
    nomes = []
    for obj in objetos:
        if isinstance(obj, dict) and 'nome' in obj:
            nomes.append(obj['nome'])
        else:
           
            nome = getattr(obj, 'nome', None)
            if nome is not None:
                nomes.append(nome)
    return nomes


pessoas = [{'nome': 'Ana'}, {'nome': 'Bruno'}, {'nome': 'Carla'}]
print(extrair_nomes(pessoas))
