nomes = [1, 'Maria', 'José', 'João']
print(nomes)
print('Original '+nomes[1])
nomes[1] = 'Joana'
print('Alterado '+nomes[1])
nomes.append('Isac')
print('Inserindo no final '+str(nomes))
nomes.insert(0, "Ribamar")
print("Inserindo em Qualquer Posição "+str(nomes))
nome_excluido= nomes.pop(0)
print(nomes)
print('O nome excluido foi: '+nome_excluido)
del nomes[0]
print('Exluindo com Del'+str(nomes))
nomes.pop()
print("Excluindo com pop sem parametro"+str(nomes))
nomes.remove("José")
print('Removendo por nome do elemento'+str(nomes))
