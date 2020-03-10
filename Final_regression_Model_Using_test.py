import pickle
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

def getScore_Using_Regression_Model():

    datafile_original = open(r"C:/Users/sajith/PycharmProjects/fyp/datacsv/normalize.csv", "r", encoding="utf-8")
    data_set = pd.read_csv(datafile_original)

    feature_cols = data_set[['Page_Rank','Hub','Similarity','No_of_post','length_in_comment','updatness','Info_Score','Emo_Score']]
    name_cols = data_set[['Username']]

    pf = PolynomialFeatures(degree=2, include_bias=True)
    pf.fit(feature_cols)

    Z_pf = pf.transform(feature_cols)

    X = feature_cols.values
    namevalue = name_cols.values

    Multiple_Regression="multiple_Regression_model.sav"
    RandomForest_Regression= "Random_Forest_Regression_model.sav"
    polynormial_Regression = "Polynormial_Regression_model.sav"

    #import saved regression models

    loaded_model_MLR = pickle.load(open(Multiple_Regression, 'rb'))
    loaded_model_RFR= pickle.load(open(RandomForest_Regression, 'rb'))
    loaded_model_PR = pickle.load(open(polynormial_Regression, 'rb'))

    result_MLR = loaded_model_MLR.predict(X)
    result_RFR = loaded_model_RFR.predict(X)
    result_PR = loaded_model_PR.predict(Z_pf)

    df_predict_MLR = pd.DataFrame({'Predicted_MLR': result_MLR})
    df_predict_RFR= pd.DataFrame({'Predicted_RFR': result_RFR})
    df_predict_PR = pd.DataFrame({'Predicted_PR': result_PR})
    df_name = pd.DataFrame(namevalue, columns=['Username'])

    result = pd.concat([df_name, df_predict_MLR,df_predict_RFR,df_predict_PR], axis=1, join='inner')
    print(result)
    result.to_csv(r'datacsv/Final_result.csv', mode='a', index=False)

