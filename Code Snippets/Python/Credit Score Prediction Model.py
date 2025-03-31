import matplotlib 
from matplotlib import pyplot as plt

import sklearn as skl
from sklearn.datasets import fetch_openml

#From Lecture Slides: import dataset from OpenML:
#Data from: https://www.openml.org/search?type=data&sort=runs&status=active&id=31
credit_scores = fetch_openml(data_id = 31)

#https://matplotlib.org/stable/gallery/statistics/hist.html
#https://seaborn.pydata.org/tutorial.html
#https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/
#https://www.openml.org/search?type=data&status=active&id=31
#https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/
#https://medium.com/analytics-vidhya/evaluating-ml-models-precision-recall-f1-and-accuracy-f734e9fcc0d3
#https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/
"""
#Check the structure of the dataset:
print(credit_scores.data)

#From "Machine Learning Statistical Foundations Professional Certificate by Wolfram Research":
print(credit_scores.data.isnull().sum())

#from https://matplotlib.org/stable/gallery/statistics/hist.html and https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
fig, axs = plt.subplots(4, 5, sharey=True, tight_layout=True)

for i in range(0,20):
    axs[0] = hist[credit_scores.data[i]]
"""
