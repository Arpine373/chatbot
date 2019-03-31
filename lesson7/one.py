import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marriagedata= pd.read_csv("marriage.csv")#karduma csv  faylic  axyusak vorpes  dataframe

#verazel  textery  tveri orinak  male -@  saqruma 0
from sklearn import preprocessing
for column in marriagedata.columns:
    if marriagedata[column].dtype == type(object):
        le = preprocessing.LabelEncoder()
        marriagedata[column] = le.fit_transform(marriagedata[column])

print(marriagedata.shape)#tpuma  syuneri  ev  toxeri  qanak
print(marriagedata.head())#tpuma  arajin  5  toxy

X=marriagedata.drop('Status_before_Marriage',axis=1)#vercrel  em  amen  inch  baci status before  marriage  syunic,drop  asuma  jnjel
y=marriagedata['Status_before_Marriage']#vercrel em  Status  before  Marriage  syuny

print(y.head())
print(X.head())

from sklearn.model_selection import train_test_split#vercnuma   train_test  funkcian gradaranic
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)#erku  hat  listy  bajanuma  4 hat listi mi  masin  20  tokosov myus  masin  80  tokosov

print(X_train.head())

from sklearn.svm import SVC#svcna  uzum   gradaranic
svclassifier = SVC(kernel='linear')#classer  bajanox dunkcian  gzayina
svclassifier.fit(X_train, y_train)#sovoracnuma x_traini u y_traini  vra

y_pr = svclassifier.predict(X_test) #vercnuma  x  test  hashvuma  y nery voronk gruma  y pri mej

print(y_pr)

print(y_test)

from sklearn.metrics import classification_report#vercnuma  classification reporty   metrics  gradaranic
print(classification_report(y_test,y_pr))
