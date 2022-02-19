# DESAFIO-DE-PROGRAMA-O-ACADEMIA-CAPGEMINI

REPOSITÓRIO DO DESAFIO DE PROGRAMAÇÃO - ACADEMIA CAPGEMINI

QUESTÃO 1:

Inicialmente precisamos do valor n que será nossa base, para isto foi utilizado um input, para obter um valor inteiro.

Começamos então três laços de repetição que irão fazer a passagem pelas linhas, laços feitos através do for, variando sempre no range.

Primeiro laço para as n's linhas que vão ter.

Segundo laço para adicionar os espaços quando não for utilizar *.

Terceiro laço para adicionar os *.

QUESTÃO 2:

Inicialmente precisamos da string password que será analisada, para isto foi utilizado um input, para obter um valor string.

Agora criamos uma condicional utilizando IF, que irá verificar que o tamanho da senha é seguro.

Se a senha for menor que 6 caracteres necessários, o programa mostrará quantos estão faltando.

Caso esteja com um tamanho correto, o programa também irá informar

QUESTÃO 3:

Para resolver esse problema, através de muitas buscas, encontrei a função "defaultdict" da biblioteca "collections", que tem a função de agrupar informações de forma concisa em dicionários. Mais informações: https://pense-python.caravela.club/19-extra/07-defaultdict.html

Para solictar a palavra a ser analisada, utilizamos um input.

Foi criada uma lista onde serão adicionados os pares de anagramas, bem como uma variável para o tamanho da palavra para ser analisada.

A verificação foi feita através de faços FOR.

Cria um dicionáio utilizando defaultdict onde a lista será organizada. Cria substring para ser analisada. Usa o comando .join() para unir as substrings. Usa .append() para adicionar ao dicionário criado anteriormente. Por fim o comando .extend() para adicionar como elemento da lista. Após a verificação a lista "resultado" irá conter todas as subtrings que formam anagramas, dividindo o valor do tamanho da lista por 2, temos a quantidade de pares.

MUITO OBRIDADO PELA OPORTUNIDADE DESSE GRANDE APRENDIZADO.
