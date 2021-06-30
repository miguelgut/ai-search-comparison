# Aula sobre aprendizado de máquina supervisionado

### Load
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier


def extraTree():
	## Criando um modelo atraves da arvore de decisao
	modelo = ExtraTreesClassifier()
	modelo.fit(x_treino, y_treino)

	## Obtendo a acurácia total (resultados que estavam certos)
	resultado = modelo.score(x_teste, y_teste)
	print(resultado)

def decisionTree():
	## Criando um modelo atraves da arvore de decisao
	modelo = DecisionTreeClassifier()
	modelo = modelo.fit(x_treino, y_treino)

	resultado = modelo.score(x_teste, y_teste)
	print(resultado)

arquivo = pd.read_csv('wine_dataset.csv')

### Rodar uma vez: Converter texto para numérico no campo style
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

### Primeiras amostras
print(arquivo.head())

### O desfecho é a variavel Y -> coluna desfecho
y = arquivo['style']
### As variáveis preditoras são todas as colunas exceto Desfecho
x = arquivo.drop('style', axis = 1)

## Separar dados de treino e dados de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

extraTree()
decisionTree()

#### Acuracias
#
#	| Extra Tree 			| Decision Tree 		|
# 	|-----------------------|-----------------------|
#	| 0.9963065558633426	| 0.9866666666666667	|
#	| 0.9956909818405664	| 0.9841025641025641	|
#	| 0.9969230769230769	| 0.9846153846153847	|