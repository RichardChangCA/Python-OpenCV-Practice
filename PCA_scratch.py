# from : https://towardsdatascience.com/pca-explained-and-implemented-in-2-minutes-e024c832bb9cs
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

data =load_iris()
X,y,column_names = data['data'],data['target'],data['feature_names']
X =pd.DataFrame(X,columns=column_names)

# centering and scaling each column
X = (X - X.mean(axis=0)) / X.std(axis=0)
X.head()

print(f'Original data shape:{X.shape}')
C =X.values.T @ X.values
print(f'Covariance matrix shape:{C.shape}\n\n')

print(C)

# find eigenvectors and eigenvalues of the covariance matrix
from numpy.linalg import eig
eigen_values, eigen_vectors = eig(C)

# printing eigenvalue and its' corresponding eigenvector
for index, eig_value in enumerate(eigen_values):
    print(eig_value, eigen_vectors[index])

# find 2 eigenvectors with the largest eigenvalues

k = 2
projection_matrix = eigen_vectors[eigen_values.argsort()[::-1][:k]]
print(projection_matrix.shape)
print(projection_matrix)

#projecting
x_reduced = X @ projection_matrix.T

print(x_reduced.shape)
print(x_reduced.head())

import matplotlib.pyplot as plt

plt.scatter(x_reduced.iloc[:, 0], x_reduced.iloc[:, 1])
plt.show()