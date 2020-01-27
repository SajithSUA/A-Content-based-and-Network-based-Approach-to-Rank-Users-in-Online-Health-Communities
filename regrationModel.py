import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sb
from sklearn import metrics

datafile = open('C:/Users/sajith/Desktop/normalize.csv', 'r',encoding="utf-8")
data_set = pd.read_csv(datafile)

feature_cols = data_set[['Page_Rank','Hub','Authority','Similarity','No_of_post']]

X = feature_cols.values
y = data_set.iloc[:, 5].values
print(y)

plt.figure(figsize=(15, 10))
plt.tight_layout()
sb.distplot(data_set['Score'])
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# print the coefficients
print('intercept: \n', regressor.intercept_)
print('coefficient: \n', regressor.coef_)

#coefficient for each feature
coeff_df = pd.DataFrame(regressor.coef_, feature_cols.columns, columns=['Coefficient'])
print(coeff_df)

# compare actual vs. predicted rank
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
compared_df = df.head(25)
print(compared_df)

compared_df.plot(kind='bar', figsize=(10, 8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))