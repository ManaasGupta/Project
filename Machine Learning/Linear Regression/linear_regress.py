#importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Fetching Data 
df = pd.read_csv("Ecommerce Customers")
print(df.head())

print(df.describe())
print(df.info())

#Visulalizing Data 
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=df)
plt.show()
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=df)
plt.show()
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=df)
plt.show()
sns.pairplot(df)
plt.show()
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=df)
plt.show()

#Splitting data into Train and Test
y = df['Yearly Amount Spent']
X = df[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Cretaing and buliding a model for Linear Regression
lm = LinearRegression()
lm.fit(X_train,y_train)
# Printing Coefficents
print('Coefficients: \n', lm.coef_)
predictions = lm.predict( X_test)
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()
# calculate these metrics by hand!
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.distplot((y_test-predictions),bins=50);
plt.show()

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients)
