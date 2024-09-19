nome = input("insira seu nome: ")
print(f"Olá, {nome} seja bem vindo ao nosso site!")
idade = int(input("coloque a sua idade: "))

if idade >= 18:
    print("Esse site contém conteúdo sensível!")
else:
    print("Você não pode entrar nesse site!")
    
verificacao = input("Resolva o seguinte problema para certificarmos que você é um humano: 29 - 13: ")
if verificacao == '16':
    print("Acerto mizeravi!")
else:
    print("Errado, tente outra vez!")