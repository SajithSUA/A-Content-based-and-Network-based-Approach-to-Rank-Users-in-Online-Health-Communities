import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import seaborn as sb
import os
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
import pickle

dataset='C:/Users/sajith/Desktop/project/test score genaration/score7.csv'

def remove_existing_SAV():
    files="C:/Users/sajith/PycharmProjects/fyp"
    for file1 in os.listdir(files):
        if file1.endswith('.sav'):
            os.remove(files + '/' + file1)

def accurency_metrics(y_test, y_pred,name):
    print(name+" reggression accurency metrics")
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    #print('R squared:', np.sqrt(metrics.r2_score(y_test, y_pred)))


def create_accurency(y_test, y_pred,name):
    print(name + " reggression accurency metrics")
    # check acccurency
    errors = abs(y_pred - y_test)
    print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')

    # Calculate mean absolute percentage error (MAPE)
    mape = 100 * (errors / y_test)
    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

def multiple_Leniear_Regression(X_train, X_test, y_train, y_test,feature_cols):
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #save model
    filename="multiple_Regression_model.sav"
    pickle.dump(regressor,open(filename,'wb'))

    # coefficient for each feature
    coeff_df = pd.DataFrame(regressor.coef_, feature_cols.columns, columns=['Coefficient'])
    print(coeff_df)
    y_pred_MLR = regressor.predict(X_test)

    print("multiple linear regression model")
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_MLR})
    compared_df = df.head(25)
    print(compared_df)
    accurency_metrics(y_test, y_pred_MLR, "Multiple linear")
    #create_accurency(y_test, y_pred_MLR, "Multiple linear")
    return y_pred_MLR

def Random_forest_regression(X_train, X_test, y_train, y_test):
    regressor = RandomForestRegressor(n_estimators=500)
    regressor.fit(X_train, y_train)

    # save model
    filename = "Random_Forest_Regression_model.sav"
    pickle.dump(regressor, open(filename, 'wb'))

    y_pred_RFLR = regressor.predict(X_test)

    print("Random Forest regression model")
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_RFLR})
    compared_df = df.head(25)
    print(compared_df)
    accurency_metrics(y_test, y_pred_RFLR, "Random Forest")
    #create_accurency(y_test, y_pred_RFLR, "Random Forest")
    return y_pred_RFLR

def polynomial_regression(feature_cols,y):
    pf = PolynomialFeatures(degree=2, include_bias=True)
    pf.fit(feature_cols)
    print(pf.get_feature_names())

    Z_pf = pf.transform(feature_cols)

    X_train, X_test, y_train, y_test = train_test_split(Z_pf, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # save model
    filename = "Polynormial_Regression_model.sav"
    pickle.dump(regressor, open(filename, 'wb'))

    # coefficient for each feature
    coeff_df = pd.DataFrame(regressor.coef_, pf.get_feature_names(), columns=['Coefficient'])
    print(coeff_df)
    y_pred_PR = regressor.predict(X_test)

    print("Plynomial regression model")
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_PR})
    compared_df = df.head(25)
    print(compared_df)
    accurency_metrics(y_test, y_pred_PR, "Plynomial")
    #create_accurency(y_test, y_pred_PR, "Plynomial")
    return y_pred_PR


def draw_chart(y_test,y_pred_MLR,y_pred_RFLR,y_pred_PR):
    # dreaw chart
    plt.figure(figsize=(10, 15))
    sb.distplot(y_test, hist=False, color="r", label="Actual value")
    sb.distplot(y_pred_MLR, hist=False, color="b", label="multiple linear regression")
    sb.distplot(y_pred_RFLR, hist=False, color="y", label="Random forest regression")
    sb.distplot(y_pred_PR, hist=False, color="g", label="Polynomial regression")

    plt.title('actual vs predicted valu')
    plt.ylabel('score')
    plt.xlabel('user')
    plt.show()

def main():
    datafile = open(dataset, 'r', encoding="utf-8")
    data_set = pd.read_csv(datafile)
    print(data_set)

    feature_cols = data_set[['Page_Rank','Hub','Similarity','No_of_post','length_in_comment','updatness','Info_Score','Emo_Score']]

    X = feature_cols.values
    y = data_set.iloc[:, 11].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    y_pred_MLR = multiple_Leniear_Regression(X_train, X_test, y_train, y_test, feature_cols)

    y_pred_RFLR=Random_forest_regression(X_train, X_test, y_train, y_test)

    y_pred_PR= polynomial_regression(feature_cols,y)


    draw_chart(y_test, y_pred_MLR,y_pred_RFLR,y_pred_PR)


if __name__ == '__main__':
    main()






