## Programa para determinar qual seção um produto deve ser armazenado
from sklearn import tree

# Treino: Produtos
Alimento = 0
Legume = 1
Liquido = 2

Branco = 0
Verde = 1
Vermelho = 2
Amarelo = 3

def Treino():
	## Estrutura do treino: Peso, Perecivel, Categoria, Cor ##
	return [
		[1, 0, Alimento,	Branco],	# Arroz
		[0.7, 1, Legume,	Verde],		# Maçã
		[5, 0, Alimento,	Vermelho],	# Arroz
		[0.5, 0, Liquido,	Verde],		# Detergente
		[0.5, 1, Legume,	Vermelho],	# Tomates
		[5, 0, Liquido,	Verde],			# Sabão
		[1, 0, Liquido,	Amarelo],		# Sabão
		[0.2, 1, Alimento,	Amarelo],	# Queijo
		[3, 1, Alimento,	Vermelho],	# Carne
		[0.5, 1, Alimento,	Branco]		# Queijo
	]

breed = Treino()

# Resposta: Prateleira
Basicos = 0
Limpeza = 1
Refrigerados = 2

result = [
	Basicos,
	Basicos,
	Basicos,
	Limpeza,
	Basicos,
	Limpeza,
	Limpeza,
	Refrigerados,
	Refrigerados,
	Refrigerados
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(breed, result)

### Testes

def Testes():
	return  [									# Produtos 		Resultado esperado
		[0.5,	1,		Legume,		Vermelho], 	# Maçã			Basicos		
		[10,	0,		Alimento,	Vermelho], 	# Arroz			Basicos		
		[1,		1,		Legume,		Vermelho], 	# Tomates		Basicos		
		[2,		0,		Liquido,	Branco] ,	# Detergente	Limpeza		
		[3,		0,		Liquido,	Verde] 	,	# Sabão			Limpeza		
		[1,		1,		Alimento,	Amarelo] ,	# Queijo		Refrigerados	
		[0.5,	0,		Liquido,	Amarelo] ,	# Sabão			Limpeza		
		[5,		1,		Alimento,	Vermelho], 	# Carne			Refrigerados	
	]

resultTeste = clf.predict(Testes())

for r in resultTeste:
	if r == Basicos:
		print("Basicos")
	elif r == Limpeza:
		print("Limpeza")
	elif r == Refrigerados:
		print("Refrigerados")
	else:
		print("Nao encontrado")