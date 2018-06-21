"""
John Widner
06-21-18
ICP 6
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, svm
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, average_precision_score, f1_score
from sklearn.naive_bayes import GaussianNB as Guass
from sklearn.neighbors import KNeighborsClassifier
import pandas

"""Question 1"""
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split data into test and train sets 50/50
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
model = Guass()
model.fit(X_test, y_test)
print(cross_val_score(model, X_test, y_test, cv=10))

"""Question 2"""

stocks = pandas.read_csv('sample_stocks.csv')

K_mean = KMeans(n_clusters=3)
K_mean.fit(stocks)
y_kmeans = K_mean.predict(stocks)
center = K_mean.cluster_centers_

plt.scatter(stocks.returns, stocks.dividendyield, c=y_kmeans)
plt.scatter(center[:, 0], center[:, 1], c='black', s=30)
plt.xlabel('returns')
plt.ylabel('dividendsyields')
plt.show()
















