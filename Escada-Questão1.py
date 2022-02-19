#inicialmente precisamos do valor n que será nossa base.
n = int(input("Digite qual o tamanho da base da escada:"))

#começamos então três laços de repetição que irão fazer a passagem pelas linhas.
for i in range(0,n):    #primeiro laço para as n's linhas que vão ter.
    for j in range(0, 4-i):     #segundo laço para adicionar os espaços quando não for utilizar *.
        print(end=" ")
    for k in range(0,i+1):      #terceiro laço para adicionar os *.
        print("*", end ="")
    print("\r")