from sklearn import preprocessing
import numpy as np
X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
X_scaled = preprocessing.normalize(X_train)

print(X_scaled)