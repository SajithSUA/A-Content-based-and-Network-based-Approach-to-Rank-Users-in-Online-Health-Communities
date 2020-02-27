import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import seaborn as sb
from sklearn import metrics

datafile = open('C:/Users/sajith/Desktop/project/test score genaration/score2.csv', 'r',encoding="utf-8")
data_set = pd.read_csv(datafile)

feature_cols = data_set[['Page_Rank','Hub','Similarity','No_of_post']]
y=data_set[['score']]
X = feature_cols.values
y = data_set.iloc[:, 7]

pf=PolynomialFeatures(degree=2,include_bias=False)
pf.fit(feature_cols)
print(pf.get_feature_names())

Z_pf= pf.transform(feature_cols)

print(feature_cols.shape)
print(Z_pf.shape)

X_train, X_test, y_train, y_test = train_test_split(Z_pf, y, test_size=0.2, random_state=0)

pr=LinearRegression()
pr.fit(X_train,y_train)

# print the coefficients
print('intercept: \n', pr.intercept_)
print('coefficient: \n', pr.coef_)

#coefficient for each feature
coeff_df = pd.DataFrame(pr.coef_, pf.get_feature_names(), columns=['Coefficient'])
print(coeff_df)

y_pred = pr.predict(X_test)
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

print('Accuracy of multiple regression classifier on test set: {:.2f}'.format(pr.score(X_test, y_test)))

plt.figure(figsize=(10,15))
sb.distplot(y_test,hist=False,color="r",label="Actual value")
sb.distplot(y_pred,hist=False,color="b",label="preddicted value")

plt.title('actual vs predicted valu')
plt.ylabel('score')
plt.xlabel('user')

plt.show()
