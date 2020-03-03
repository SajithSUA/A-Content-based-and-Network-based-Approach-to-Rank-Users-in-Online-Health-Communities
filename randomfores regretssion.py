
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import seaborn as sb
from sklearn import metrics

datafile = open('C:/Users/sajith/Desktop/project/test score genaration/score3.csv', 'r',encoding="utf-8")
data_set = pd.read_csv(datafile)

feature_cols = data_set[['Page_Rank','Hub','Authority','Similarity','No_of_post','length_in_comment']]

X = feature_cols.values
y = data_set.iloc[:, 7].values
print(y)

plt.figure(figsize=(15, 10))
plt.tight_layout()
sb.distplot(data_set['score'])
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X_train, y_train)

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


#check acccurency
errors = abs(y_pred - y_test)
print('Metrics for Random Forest Trained on Original Data')
print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')



datafile1 = open('C:/Users/sajith/Desktop/normalize.csv', 'r',encoding="utf-8")
data_set1 = pd.read_csv(datafile1)


plt.figure(figsize=(10,15))
sb.distplot(y_test,hist=False,color="r",label="Actual value")
sb.distplot(y_pred,hist=False,color="b",label="preddicted value")

plt.title('actual vs predicted valu')
plt.ylabel('score')
plt.xlabel('user')

plt.show()