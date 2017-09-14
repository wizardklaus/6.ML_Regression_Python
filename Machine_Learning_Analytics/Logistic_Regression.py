# package import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# data loading
train=pd.read_csv('train.csv')
# columns=pd.DataFrame.col[0, 6, 7, 19, 20, 21, 22]
train=train.drop(train.columns[[0, 6, 7, 19, 20, 21, 22]], axis=1)
test=pd.read_csv('test.csv')
test=test.drop(test.columns[[0, 6, 7, 19, 20, 21, 22]], axis=1)

X_train=train.drop('impression', axis=1)
# Y_train=pd.DataFrame(columns=['impression'])
Y_train=train['impression'] #impression is 0 or 1 (bad or good impression)

X_val=test.drop('impression', axis=1)
Y_val=test['impression']

# logistic regression
logreg=LogisticRegression()
logreg.fit(X_train, Y_train)
# Y_pred=logreg.predict(X_val)
acc_training=round(logreg.score(X_train, Y_train)*100, 2)
acc_validation=round(logreg.score(X_val, Y_val)*100, 2)
print("training_acc : ", acc_training, "  ", "validation_acc : ", acc_validation)
# print ("training acc : ", acc_training)