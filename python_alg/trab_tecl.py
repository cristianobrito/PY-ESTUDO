nota01 = int(input('Digite a  primeira nota: '))
nota02 = int(input('Digite a segunda nota: '))
print(nota01, " ", nota02)
media = (nota01 + nota02) / 2
print(media)
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
