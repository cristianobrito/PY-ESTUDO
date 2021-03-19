def ola():  # cabeçalho
    nome = input('Digite seu nome: ')
    print('Olá ', nome)

parar = 'n'
while parar == 'n':
    ola()
    parar = input('Deseja parar? Digite n para Não ou qualquer tecla para Sim')


