import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_pickle('data/dfClean')
df.head()


x1 = df['budget'].tolist()
x2 = df['directorRaiting'].tolist()
x3 = df['castPopularity'].tolist()
x4 = df['genreEncoded'].values
x4 = x4.tolist()


y = df['vote_average'].tolist()
X = []
for i in range(0, len(x1)):
    X.append([x1[i], x2[i], x3[i], x4[i]])


le = LabelEncoder()
b = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, b, test_size=0.5, random_state=42)


isf = IsolationForest(n_jobs=-1, random_state=1)
isf.fit(X_train, y_train)
a = isf.predict(X).tolist()
b = b.tolist()

i = 0
while True:
    if i == len(X):
        break
    else:
        if a[i] == -1:
            a.pop(i)
            X.pop(i)
            b.pop(i)
        i += 1

X_train, X_test, y_train, y_test = train_test_split(X, b, test_size=0.5, random_state=42)

tr = DecisionTreeRegressor(random_state=42)
tr.fit(X_train, y_train)

prediction = tr.predict(X_test).tolist()

for i in range(0, len(prediction)):
    prediction[i] = int(prediction[i])

predictionLabeled = []
for i in range(0, len(prediction)):
    predictionLabeled.append(le.inverse_transform([prediction[i]]))
y_testLabeled = []
for i in range(0, len(y_test)):
    y_testLabeled.append(le.inverse_transform([y_test[i]]))

for i in range(len(y_testLabeled)):
    y_testLabeled[i] = int(y_testLabeled[i])

def predictor(budjet, dirRaiting, castPopular, genre):
    return tr.predict([[budjet, dirRaiting, castPopular, genre]]), mean_squared_error(y_testLabeled, predictionLabeled)
