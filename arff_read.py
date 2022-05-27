#Nome: Bryan Jonathan Melo De Oliveira
from scipy.io import arff
import pandas as pd


#Ler arquivo arff
data = arff.loadarff("iris.arff")
df = pd.DataFrame(data[0])
print(df)

#Entrar com a quantidade de clusters
try:
    k = int(input('Quantos clusters? :'))
except ValueError:
    print("Not a number")

#Centroides aleatorios
df2 = df.sample(k)
#print(df2)

#Para cada linha em df
for i in range(len(df)):
    #Setar o primeiro int para 0
    x = 0
    #Para cada centroide
    for j in range(len(df2)):
        #Se for o primeiro valor adicionar a tupla desse centroid
        if x == 0:
            df2 += df.loc[i]
        #Senao
        else:
            #Definir temporario como o x
            v = x
            #Fazer o calculo do x novo subtraindo o valor do centroid o valor de i
            x = df2[j].sub(i)
            #Se o valor do x for menor que v(valor antigo) a distancia é menor, entao eu adiciono ao centroid atual
            if x < v:
                df2 += df.loc[i]

print(df2)