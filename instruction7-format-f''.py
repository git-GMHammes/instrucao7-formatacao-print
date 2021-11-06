nome = 'Gustavo Hammes'
idade = 44
altura = 1.68
e_maior = idade >18
data_atual = 2019
peso = 89
imc = peso/(altura**2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
