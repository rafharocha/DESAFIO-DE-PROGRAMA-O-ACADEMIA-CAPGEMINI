#inicialmente precisamos da string password que será analisada.
password = str(input("Digite sua senha:"))

#agora criamos uma condicional que irá verificar que o tamanho da senha é seguro.
if (len(password)<6):   #se a senha for menor que 6 caracteres necessários, o programa mostrará quantos estão faltando.
    print("Essa senha não é segura, adicione pelo menos mais", (6-len(password)), "caracteres")
else:       #caso esteja com um tamanho correto, o programa também irá informar.
    print("Sua senha está com um ótimo tamanho!")