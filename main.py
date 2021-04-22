import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
import graphviz
criteria = ['gini','entropy']
depth = [3,5,7]
X = pd.DataFrame(pd.read_excel('bialaczka.XLS').fillna(0)).values
ansTraining=[]
dataTraining = []
dataTesting = []
ansTesting = []
ans = []
data = []

for i in range (len(X)):
    data.append([X[i][20], X[i][19], X[i][15], X[i][3], X[i][7], X[i][2], X[i][17], X[i][11], X[i][4]])
    ans.append(X[i][0])
dataTraining, dataTesting, ansTraining, ansTesting = train_test_split(data, ans, test_size = 0.5, random_state=0)

for crit in criteria:
    print(crit)
    for num in depth: 
        clf = tree.DecisionTreeClassifier(criterion=crit, max_depth=num) 
        print('max dept = ' + str(num))

        clf = clf.fit(dataTraining, ansTraining)
        score = cross_val_score(estimator=clf, X=dataTesting, y=ansTesting, cv=5, n_jobs=4)

        print(score.mean())
        print('----------------------------------------------')
        print(cross_val_predict(clf, dataTesting, ansTesting))
        print('----------------------------------------------')













