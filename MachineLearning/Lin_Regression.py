import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
customers = pd.read_csv(r'C:\Users\Hovo\Desktop\pythonprojects\MachineLearning\data\Ecommerce Customers')

#data analysis
print(customers.head())
print(customers.info())
print(customers.describe())
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)
sns.pairplot(customers)
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)
plt.show()
#splitting data
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#training model
lm = LinearRegression()
lm.fit(X_train,y_train)
print('Coefficients: \n', lm.coef_)

#applying to test set
predictions = lm.predict(X_test)

#checking results
plt.scatter(y_test,predictions)
plt.show()
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients.head())