for i in range (trait):
	for j in range (len(clf)):
		for k in range (len(clf)):
			t[i][j][k], p[i][j][k]=ttest_ind(results[j+i*6],results[k+i*6])


for index, t in enumerate(t):
	advantages[index][t > 0] = 1


for index, p_value in enumerate(p):
	importance[index][p_value <= alpha] = 1


for i in range(trait):
	betterStat.append(importance[i] * advantages[i])

print(t)
print('\n')
print(p)
print('\n')
print(advantages)
print('\n')
print(importance)
print('\n')
print(betterStat)