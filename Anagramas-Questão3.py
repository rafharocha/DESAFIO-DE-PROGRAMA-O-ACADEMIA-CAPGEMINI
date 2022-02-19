from collections import defaultdict #Para resolver esse problema, encontrei essa função da biblioteca collections, sua usabilidade pode ser vista no README.

palavra = str(input("Digite a palavra que será analisada:")) #Para solictar a palavra a ser analisada.
resultado = []  #Uma lista onde serão adicionados os pares de anagramas.
tamanho = len(palavra) #tamanho da palavra para ser analisada.

#inicia então a verificação através de laços.
for i in range(1, tamanho + 1):
    dicionario = defaultdict(list) #Cria um dicionáio onde a lista será organizada.
    for j in range(tamanho - i + 1):
        ss = palavra[j : j + i]     #Cria substring para ser analisada.
        k = "".join(sorted(ss))     #Para unir as substrings.
        dicionario[k].append(ss)    #Para adicionar ao dicionário criado anteriormente.
    for k, v in dicionario.items(): #Novo laço para percorrer os itens do dicionário.
        if len(v) >= 2:
            resultado.extend(v)     #para adicionar como elemento da lista.
quantidade = int(len(resultado)/2)  #por fim a lista resultado irá conter todas as subtrings que formam anagramas, dividindo o valor do tamanho da lista por 2, temos os pares.
print(quantidade)