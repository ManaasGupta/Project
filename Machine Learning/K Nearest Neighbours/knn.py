#importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

#Fetching data
df=pd.read_csv('Classified Data',index_col=0)

df.head()
#standardize in case of knn

scaler=StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_features=scaler.transform(df.drop('TARGET CLASS',axis=1))
scaled_features
df_feat=pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat

#Splitting data in Train and Test
X=df_feat
y=df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Calling Knn Instance and bulding model with n_neighbors=1
knn_model=KNeighborsClassifier(n_neighbors=1)
knn_model.fit(X_train,y_train)
pred=knn_model.predict(X_test)

#Evaluating results before chossing best n_neighbors
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

#choosing correct K value
error_rate=[]
for i in range(1,40):
    knn_model2=KNeighborsClassifier(n_neighbors=i)
    knn_model2.fit(X_train,y_train)
    predict_i=knn_model2.predict(X_test)
    error_rate.append(np.mean(predict_i != y_test))
print(f'Minumum Error Rate is {np.min(error_rate)}')
print(f'Index at which error rate is Minimum is {np.argmin(error_rate)}')
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='b',linestyle='dashed',marker='o',markerfacecolor='r',markersize=10)
plt.title('Error Rate vs K_Value')
plt.xlabel('x')
plt.ylabel('Error Rate')
plt.show()

#Appling and buliding knn nn_neighbors= Minumum Error Rate Index
knn_model2=KNeighborsClassifier(n_neighbors=np.argmin(error_rate))
knn_model2.fit(X_train,y_train)
predict_i=knn_model2.predict(X_test)
#Evaluating results after chossing best n_neighbors
print(confusion_matrix(y_test,predict_i))
print(classification_report(y_test,predict_i))
