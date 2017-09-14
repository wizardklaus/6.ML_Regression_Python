# package import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# data loading
df=pd.read_csv('clean_data01.csv')
# X=df.iloc[,0:81]
# y=df.iloc[,82]
X=df.drop('flag', axis=1)
Y=df['flag']
X_train,X_val,Y_train,Y_val=train_test_split(X, Y, test_size=0.2, random_state=5)
# combine=[train_df,test_df]

# # modeling
# X_train=train_df.drop('y',axis=1)
# Y_train=train_df['y']
# X_val=test_df.drop('y',axis=1)
# Y_val=test_df['y']

# logistic regression
logreg=LogisticRegression()
logreg.fit(X_train, Y_train)
#Y_pred=logreg.predict(X_val)
acc_training=round(logreg.score(X_train, Y_train)*100, 2)
acc_validation=round(logreg.score(X_val, Y_val)*100, 2)
print("training_acc : ", acc_training, "  ", "validation_acc : ", acc_validation)