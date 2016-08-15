import numpy as np
from sklearn import svm
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from reader import *

#shape data into smaller matrix
x = Amatrix[:-30000]
b = bvector[:-30000]

#train classifier
C_range = np.logspace(-2,10,13)
gamma_range = np.logspace(-9,3,13)
param_grid = dict(gamma=gamma_range, C=C_range)
cv = StratifiedShuffleSplit(b, n_iter = 5, test_size=0.2,random_state=42)
grid = GridSearchCV(SVC(), param_grid, cv=cv)
grid.fit(x, b)

print("The best parameters are %s with a score of %0.2f" % (grid.best_params_,grid.best_score))

