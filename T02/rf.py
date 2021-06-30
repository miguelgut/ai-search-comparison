import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

global LE
LE = preprocessing.LabelEncoder()

def randomForestScore(x_treino, x_teste, y_treino, y_teste):
	## Criando um modelo atraves da arvore de decisao
	modelo = RandomForestClassifier(n_estimators=100)
	modelo = modelo.fit(x_treino, y_treino)
	resultado = modelo.score(x_teste, y_teste)
	return resultado

def optimizeColumn(arquivo):
	print('Aperfeiçoando coluna: \n')

	uniqueGenre = pd.DataFrame({
		'genre': arquivo.Genre.unique(),
	})

	genre_dummy = uniqueGenre['genre'].str.get_dummies(sep=',')
	arquivo.drop(columns=['Actor', 'Genre', 'Unnamed: 0', 'Metascore', 'Description'], inplace=True)
	arquivo = pd.concat([arquivo, genre_dummy], axis=1)

	print(arquivo.head())
	return arquivo

def optimizeNan(arquivo):
	print('Aperfeiçoando NaN: \n')
	print('Total Rows:' + str(len(arquivo.index)))
	print('NaN Year: ' + str(arquivo['Year'].isna().sum()))
	print('NaN RT: ' + str(arquivo['RunTime'].isna().sum()))
	print('NaN Rating: ' + str(arquivo['Rating'].isna().sum()))
	print('NaN IMDB_Score: ' + str(arquivo['IMDB_Score'].isna().sum()))

	arquivo.fillna(arquivo.mean(), inplace=True)
	print(arquivo.head())
	return arquivo

## Função que carrega o CSV e prepara os arquivos para a execução do código
def prepare():
	### Lendo arquivo
	arquivo = pd.read_csv('database.csv')

	arquivo = optimizeNan(arquivo)
	arquivo = optimizeColumn(arquivo)

	for column_name in arquivo.columns:
	    if arquivo[column_name].dtype == object:
	        arquivo[column_name] = LE.fit_transform(arquivo[column_name])
	    else:
	        pass


	### Remove os NaN
	arquivo = arquivo.replace(np.nan, False, regex=True)
	### Primeiras amostras
	print(arquivo.head())
	return arquivo


def main():	

	database = prepare()

	desfecho = 'IMDB_Score'
	### O desfecho é a variavel Y -> coluna IMDB_Score
	y = database[desfecho]
	y = pd.Series(LE.fit_transform(y))

	### As variáveis preditoras são todas as colunas exceto Desfecho
	x = database.drop(desfecho, axis = 1)
	
	i = total = 0
	while i < 10:
		## Separar dados de treino e dados de teste
		x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
		result = randomForestScore(x_treino, x_teste, y_treino, y_teste)
		print("Iteração  "+ str(i+1) + "\t " + str(result))
		total += result
		i += 1

	print("Acuracia Média \t" + str(total/i))

main()