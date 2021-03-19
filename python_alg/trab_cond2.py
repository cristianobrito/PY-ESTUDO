# notas 0 - 10, aprovado >=6.0 , recuperação >= 4.0 e < 6.0
# reprovado >0 < 4.0
nota = 4
if (nota >= 6.0) and (nota <= 10):
    print('Foi aprovado')
elif (nota >= 4.0) and (nota < 6.0):
    print('Você pode fazer a recuperação')
elif (nota >0) and (nota < 4.0):
    print("Você foi reprovado")
else:
    print("Digite um valor entre 0 - 10")
