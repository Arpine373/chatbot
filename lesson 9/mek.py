motivation=['are','are not','are']
health=['yes','no','yes']
gnumasporti=['yes','no','no']
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
motivation_encoded=le.fit_transform(motivation)
print(motivation_encoded)
health_encoded=le.fit_transform(health)
print("Health:",health_encoded)
features=list(zip(motivation_encoded,health_encoded))
print(features)
label=le.fit_transform(gnumasporti)
print(label)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,1]])
print("Predicted value:",predicted)

