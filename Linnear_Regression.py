import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sb
from sklearn import metrics
import pickle

def Model_Build():
    datafile = open(r"G:\FYP\feature_set\Normalized_features_model.csv", "r",encoding="utf-8")
    data_set = pd.read_csv(datafile)

    feature_cols = data_set[['Datefeature','trendingfeature','LDAfeature']]

    X = feature_cols.values
    y = data_set.iloc[:, 3].values
    print(y)

    plt.figure(figsize=(15, 10))
    plt.tight_layout()
    sb.distplot(data_set['Updateness'])
    # plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    #create model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #save model to disk
    filename = 'finalized_model.sav'
    pickle.dump(regressor, open(filename, 'wb'))


    # print the coefficients
    print('intercept: \n', regressor.intercept_)
    print('coefficient: \n', regressor.coef_)

    #coefficient for each feature
    coeff_df = pd.DataFrame(regressor.coef_, feature_cols.columns, columns=['Coefficient'])
    print(coeff_df)

    # compare actual vs. predicted rank
    y_pred = regressor.predict(X_test)
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


def Predict_Score():
    datafile_original = open(r"E:\FYP\CSV_files\Normalized_features_model_original.csv", "r", encoding="utf-8")
    data_set = pd.read_csv(datafile_original)

    feature_cols = data_set[['Date_feature', 'trending_feature', 'LDA_feature']]
    name_cols = data_set[['name']]

    X = feature_cols.values
    namevalue = name_cols.values

    # load model and predict new result
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    result = loaded_model.predict(X)
    df_predict = pd.DataFrame({'Predicted': result})
    df_name = pd.DataFrame(namevalue, columns=['Name'])

    result = pd.concat([df_name, df_predict], axis=1, join='inner')
    print(result)
    result.to_csv(r'CSV_files\Final_result.csv', mode='a', index=False)