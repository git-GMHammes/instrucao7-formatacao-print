
# Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa,
# Criar variável com o ano atual (int),
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-String (com chaves)

nome = 'Gustavo Hammes'
idade = 44
altura = 1.69
peso = 89.6
ano_atual = 2021
ano_nascimento = ano_atual-idade
imc = peso/(altura**2)
print(f'Os Valores exibidos são:')
print(f'nome: {nome}, idade: {idade}, altura: {altura}, peso: {peso}')
print('O ano de nacimento do {}, é: {} e seu IMC é: {:.2f}'.format(nome, ano_nascimento, imc))
