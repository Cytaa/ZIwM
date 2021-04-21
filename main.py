import pandas as pd
import numpy as np
from sklearn import tree
import graphviz

X = pd.DataFrame(pd.read_excel('bialaczka.XLS').fillna(0)).values
trainingAns=[]
trainingData = []
ans = []

for i in range (len(X)):
    trainingData.append([X[i][20], X[i][19], X[i][15], X[i][3], X[i][7], X[i][2], X[i][17], X[i][11], X[i][4]])
    trainingAns.append(X[i][0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(trainingData, trainingAns)
ans = clf.predict(trainingData)

# print('tutaj odpowiedzi')
# print(ans)
# print('tutaj dane testowe')
# print(trainingData)
# print('siema tutaj odpowiedzi')
print(ans)










