from numpy import matrix
import pandas as pd
from scipy import stats
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from scipy import stats

criteria = ['gini','entropy']
depth = [3,5,7]
X = pd.DataFrame(pd.read_excel('bialaczka.XLS').fillna(0)).values
ansTraining=[]
dataTraining = []
dataTesting = []
ansTesting = []
ans = []
data = []
bestResults = [0,0,0,0,0,0]
for i in range(0,5):
    for i in range (len(X)):
        data.append([X[i][20], X[i][19], X[i][15], X[i][3], X[i][7], 
        X[i][2], X[i][17], X[i][11], X[i][4]])
        ans.append(X[i][0])
    dataTraining, dataTesting, ansTraining, ansTesting = train_test_split(data, ans, test_size = 0.5, random_state=2)

    for crit in criteria:
        print(crit)
        for num in depth: 
            clf = tree.DecisionTreeClassifier(criterion=crit, max_depth=num) 
            print('max dept = ' + str(num))

            clf = clf.fit(dataTraining, ansTraining)
            score = cross_val_score(estimator=clf, X=dataTesting, y=ansTesting, cv=5, n_jobs=4)

            scoreValue = score.mean()
            print(scoreValue)
            print('----------------------------------------------')
            if(crit == criteria[0]):
                if(num == depth[0] and scoreValue > bestResults[0]): bestResults[0] = scoreValue
                if(num == depth[1] and scoreValue > bestResults[1]): bestResults[1] = scoreValue
                if(num == depth[2] and scoreValue > bestResults[2]): bestResults[2] = scoreValue
            else:
                if(num == depth[0] and scoreValue > bestResults[3]): bestResults[3] = scoreValue   
                if(num == depth[1] and scoreValue > bestResults[4]): bestResults[4] = scoreValue
                if(num == depth[2] and scoreValue > bestResults[5]): bestResults[5] = scoreValue














