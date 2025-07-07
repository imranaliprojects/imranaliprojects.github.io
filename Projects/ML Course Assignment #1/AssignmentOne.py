import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib
from sklearn import datasets
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_curve
from sklearn import model_selection
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt

#1. Wine Using Entropy
#Database importing
wine = datasets.fetch_openml(data_id=44091)

#Initialization:
wineTreeE = DecisionTreeClassifier(criterion="entropy")

#Training
y_scores=cross_val_predict(wineTreeE, wine.data, wine.target, method="predict_proba", cv=10)

#ROC Curve:
fpr, tpr, th = roc_curve(wine.target, y_scores[:,1],pos_label="True")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr,tpr,label="Decision Tree when Parameter=1")
plt.legend()
plt.show()

#Area Under Curve
print("Area under curve when minimum number of samples in leaf is one:")
print(roc_auc_score(wine.target, y_scores[:,1]))
print("")

testParameterChoices=[100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
AUCs=[100.0,110.,120.0,130.0,140.0,150.0,160.0,170.0,180.0,190.0,200.0,210.0,220.0,230.0,240.0,250.0,260.0,270.0,280.0,290.0,300.0]
i=0
#I saw that one of the requirements was a AUC Table so I tried to make one:
while i<len(AUCs):
    wineTreeE = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=testParameterChoices[i])
    y_scores=cross_val_predict(wineTreeE, wine.data, wine.target, method="predict_proba", cv=10)
    AUCs[i]= roc_auc_score(wine.target, y_scores[:,1])
    i+=1


AUCtable=pd.Series(AUCs, index=testParameterChoices)
print(AUCtable)


#Parameter Tuning:

#after doing some testing with the minimum number of samples by myself and modifying the parameters and 'min_samples_leaf' value of best params,
#I found that 2,4,... was far too small to optimise the AUC. I wanted to try values in the 100s and a lot of them.
#Manually trying to make a table of AUC values led me to find that the parameter tuning was off;
#the AUC value was consistenly highest when the minimum number of instances at each leaf is 140.
#I also know that my attempt at a table is not efficient.

parameters = [{"min_samples_leaf":testParameterChoices}]

tunedwineTreeE = model_selection.GridSearchCV(wineTreeE, parameters,
scoring="roc_auc", cv=5)

y_scores=cross_val_predict(tunedwineTreeE, wine.data, wine.target, method="predict_proba", cv=10)
print(roc_auc_score(wine.target, y_scores[:,1]))

tunedwineTreeE.fit(wine.data, wine.target)

r=tunedwineTreeE.best_params_
{'min_samples_leaf': 300}

print(r)


#final version of wine model using calculated value for minimum samples:
#I don't believe that the resulting minimum number of samples is correct
#and would like to figure out how to do better with this.

wineTreeE = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=240)

#Training
y_scores=cross_val_predict(wineTreeE, wine.data, wine.target, method="predict_proba", cv=10)
auc="Area under curve when minimum number of samples in leaf is {}"
print(auc.format(wineTreeE.min_samples_leaf))

print(roc_auc_score(wine.target, y_scores[:,1]))

#ROC Curve:
fpr, tpr, th = roc_curve(wine.target, y_scores[:,1],pos_label="True")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr,tpr,label="Decision Tree when Parameter=240")
plt.legend()
plt.show()







#2. Wine Using Gini
print("Wine Database Using Gini")

#Intialization:
wineTreeG = DecisionTreeClassifier()

#Training
y_scoresG=cross_val_predict(wineTreeG, wine.data, wine.target, method="predict_proba", cv=10)

#ROC Curve:
fpr, tpr, th = roc_curve(wine.target, y_scoresG[:,1],pos_label="True")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr,tpr,label="Decision Tree for Gini when Parameter = 1")
plt.legend()
plt.show()

#Area Under Curve
print("Area under curve when minimum number of samples in leaf is one:")
print(roc_auc_score(wine.target, y_scoresG[:,1]))
print("")

testParameterChoicesG=[100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
AUCsG=[100.0,110.,120.0,130.0,140.0,150.0,160.0,170.0,180.0,190.0,200.0,210.0,220.0,230.0,240.0,250.0,260.0,270.0,280.0,290.0,300.0]
i2=0
#attempt to make an AUC table
while i2<len(AUCsG):
    wineTreeG = DecisionTreeClassifier(min_samples_leaf=testParameterChoices[i2])
    y_scoresG=cross_val_predict(wineTreeG, wine.data, wine.target, method="predict_proba", cv=10)
    AUCsG[i2]= roc_auc_score(wine.target, y_scoresG[:,1])
    i2+=1


AUCtableG=pd.Series(AUCsG, index=testParameterChoicesG)
print(AUCtableG)


#Parameter Tuning:

parametersG = [{"min_samples_leaf":testParameterChoicesG}]

tunedwineTreeG = model_selection.GridSearchCV(wineTreeG, parametersG,
scoring="roc_auc", cv=5)

y_scoresG=cross_val_predict(tunedwineTreeG, wine.data, wine.target, method="predict_proba", cv=10)
print(roc_auc_score(wine.target, y_scoresG[:,1]))

tunedwineTreeG.fit(wine.data, wine.target)

r2=tunedwineTreeG.best_params_

print(r2)

#The above attempt to use GridSearchCV seems to give a recommended value for the minimum number of instances at the leaves.
#this seems to the same number as for the first. I am not sure why.
#final version of wine model using calculated value for minimum samples:

wineTreeG = DecisionTreeClassifier(min_samples_leaf=240)

#Training
y_scoresG=cross_val_predict(wineTreeG, wine.data, wine.target, method="predict_proba", cv=10)
auc="Area under curve when minimum number of samples in leaf is {}"
print(auc.format(wineTreeG.min_samples_leaf))

print(roc_auc_score(wine.target, y_scores[:,1]))

#ROC Curve:
fpr2, tpr2, th2 = roc_curve(wine.target, y_scores[:,1],pos_label="True")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr2,tpr2,label="Decision Tree for Gini when Parameter = 240")
plt.legend()
plt.show()





phoneme = datasets.fetch_openml(data_id=1489)
#3. Phoneme Using Entropy:
print("")
print("")

#Initialization:
pTreeE = DecisionTreeClassifier(criterion="entropy")

#Training and testing using the cross fold method with ten folds
pScores=cross_val_predict(pTreeE, phoneme.data, phoneme.target, method="predict_proba", cv=10)

#creating an ROC Curve for when minimum number of leaves is 1.
fpr3, tpr3, th3 = roc_curve(phoneme.target, pScores[:,1],pos_label="2")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr3,tpr3,label="Decision Tree for Phoneme when number of instances per leaf node = 1")
plt.legend()
plt.show()

#Area Under Curve:
print("Area under curve when minimum number of samples in leaf is one:")
print(roc_auc_score(phoneme.target, pScores[:,1]))

#I noticed that this ROC curve was very different from any of the other curves, which made me hopeful that I was doing something right.
#I still was not sure how to make an AUC table without doing so by brute force.

#Parameter Tuning:
pParametersE = [{"min_samples_leaf":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}]

tunedpTreeE = model_selection.GridSearchCV(pTreeE, pParametersE,scoring="roc_auc", cv=5)
pScores=model_selection.cross_val_predict(tunedpTreeE,phoneme.data, phoneme.target,method="predict_proba",cv=10)

tunedpTreeE.fit(phoneme.data, phoneme.target)
print(tunedpTreeE.best_params_)

#creating final version of the model:
pTreeE = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=14)
pScores=cross_val_predict(pTreeE, phoneme.data, phoneme.target, method="predict_proba", cv=10)
fpr3, tpr3, th3 = roc_curve(phoneme.target, pScores[:,1],pos_label="2")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr3,tpr3,label="Decision Tree for Phoneme when number of instances per leaf node = 14")
plt.legend()
plt.show()
display="Area under curve when minimum number of samples in leaf is {}:"
print(display.format(pTreeE.min_samples_leaf))
print(roc_auc_score(phoneme.target, pScores[:,1]))

#I'm glad one of my ROC tables worked well.
ptestParameterChoicesE=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pAUCs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i3=0
#attempt to make an AUC table again.
while i3<len(pAUCs):
    pTreeE = DecisionTreeClassifier(min_samples_leaf=testParameterChoices[i3])
    pScores=cross_val_predict(pTreeE, phoneme.data, phoneme.target, method="predict_proba", cv=10)
    pAUCs[i3]= roc_auc_score(phoneme.target, pScores[:,1])
    i3+=1
#after looking through the AUC table, I noticed that the AUC is very different from what it should be.

pAUCtableE=pd.Series(pAUCs, index=ptestParameterChoicesE)
print(pAUCtableE)




#4. Phoneme Using Gini:

print("")
print("")

#Initialization:
pTreeG = DecisionTreeClassifier()

#Training and testing using the cross fold method with ten folds
pScoresG=cross_val_predict(pTreeG, phoneme.data, phoneme.target, method="predict_proba", cv=10)

#creating an ROC Curve for when minimum number of leaves is 1.
fpr4, tpr4, th4 = roc_curve(phoneme.target, pScoresG[:,1],pos_label="2")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr4,tpr4,label="Decision Tree for Phoneme when minimum number of instances per leaf node = 1")
plt.legend()
plt.show()

#Area Under Curve:
print("Area under curve when minimum number of samples in leaf is one:")
print(roc_auc_score(phoneme.target, pScoresG[:,1]))

#Parameter Tuning:
pParametersG = [{"min_samples_leaf":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}]

tunedpTreeG = model_selection.GridSearchCV(pTreeG, pParametersG,scoring="roc_auc", cv=5)
pScores2=model_selection.cross_val_predict(tunedpTreeG,phoneme.data, phoneme.target,method="predict_proba",cv=10)

tunedpTreeG.fit(phoneme.data, phoneme.target)
print(tunedpTreeG.best_params_)

#creating final version of the model:
pTreeG = DecisionTreeClassifier(min_samples_leaf=14)
pScoresG=cross_val_predict(pTreeG, phoneme.data, phoneme.target, method="predict_proba", cv=10)
fpr4, tpr4, th4 = roc_curve(phoneme.target, pScores2[:,1],pos_label="2")
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(fpr4,tpr4,label="Decision Tree for Phoneme when number of instances per leaf node = 14")
plt.legend()
plt.show()
display="Area under curve when minimum number of samples in leaf is {}:"
print(display.format(pTreeG.min_samples_leaf))
print(roc_auc_score(phoneme.target, pScoresG[:,1]))


ptestParameterChoicesG=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pAUCsG=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i4=0
#attempt to make an AUC table for the last time.
while i4<len(pAUCsG):
    pTreeG = DecisionTreeClassifier(min_samples_leaf=testParameterChoices[i4])
    pScoresG=cross_val_predict(pTreeG, phoneme.data, phoneme.target, method="predict_proba", cv=10)
    pAUCsG[i4]= roc_auc_score(phoneme.target, pScoresG[:,1])
    i4+=1

pAUCtableG=pd.Series(pAUCsG, index=ptestParameterChoicesG)
print(pAUCtableG)
