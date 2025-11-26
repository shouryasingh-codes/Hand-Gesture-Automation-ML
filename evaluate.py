import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble  import RandomForestClassifier
from sklearn.metrics  import accuracy_score , confusion_matrix , classification_report
import pickle
import os

file = open("guestre_model.pkl","wb")
data = pd.read_csv("VICTORY_landmark_norm.csv",header=None)
data1 = pd.read_csv("fist_landmark_norm.csv",header=None)
data2 = pd.read_csv("open_landmark_norm.csv",header=None)

data["label"] = 0
data1["label"] = 1
data2["label"] = 2
df = pd.concat([data,data1,data2])
df = df.reset_index(drop=True)

df =  df.drop(columns=[0])
x = df.drop("label",axis=1)
y = df["label"]

model = RandomForestClassifier()
X_train , X_test , Y_train , Y_test = train_test_split(x,y,test_size=0.2)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(Y_test,prediction)
confusion_matrix1 =  confusion_matrix(Y_test, prediction)
classification_report1 =  classification_report(Y_test, prediction)
pickle.dump(model,file)
print(accuracy)
print(confusion_matrix1)
print(classification_report1)

file.close()
