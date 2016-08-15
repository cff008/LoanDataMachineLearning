import numpy as np
from sklearn import svm
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from reader import *

#shape data into smaller matrix
x = Amatrix[:-7900]
b = bvector[:-7900]
print(b)
xTest = Amatrix[-7900:]
yTest = bvector[-7900:]

SVC(C=1.0,cache_size=600, class_weight=None, coef0=0.0, decision_function_shape=None,
 	degree=3,gamma='auto',kernel='rbf',max_iter=-1,probability=False,random_state=None,
 	shrinking=True,tol=0.001,verbose=False)

clf = SVC()
clf.fit(x,b)
predicted = clf.predict(xTest)

# neg = 0;
# for i in range(len(yTest)):
# 	if yTest[i] < 0:
# 		neg = neg +1

# neg = neg/(len(yTest))
# print(neg)
for i in range(len(predicted)):
	print(predicted[i])
print accuracy_score(yTest, predicted)

#train classifier
# C_range = np.logspace(-2,10,13)
# gamma_range = np.logspace(-9,3,13)
# param_grid = dict(gamma=gamma_range, C=C_range)
# cv = StratifiedShuffleSplit(b, n_iter = 5, test_size=0.2,random_state=42)
# grid = GridSearchCV(SVC(), param_grid, cv=cv)
# grid.fit(x, b)

# print("The best parameters are %s with a score of %0.2f" % (grid.best_params_,grid.best_score))

