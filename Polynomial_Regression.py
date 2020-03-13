# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sb
from sklearn import metrics
# Importing the dataset
data_set = pd.read_csv(r"G:\FYP\feature_set\Normalized_features_model.csv")

feature_cols = data_set[['Datefeature', 'trendingfeature', 'LDAfeature']]
X = feature_cols.values
y = data_set.iloc[:, 3].values

from sklearn.linear_model import LinearRegression

lin = LinearRegression()

lin.fit(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X_train)
X_poly_test = poly.fit_transform(X_test)

poly.fit(X_poly, y_train)
lin2 = LinearRegression()
lin2.fit(X_poly, y_train)

plt.figure(figsize=(15, 10))
plt.tight_layout()
sb.distplot(data_set['Updateness'])

y_pred = lin2.predict(X_poly_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
compared_df = df.head(20)
print(compared_df)

compared_df.plot(kind='bar', figsize=(10, 8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))