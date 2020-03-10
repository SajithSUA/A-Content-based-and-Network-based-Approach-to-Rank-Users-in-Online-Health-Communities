import numpy as np
import pandas as pd
from sklearn import preprocessing
def Normalized_features():
    with open(r"E:\FYP\CSV_files\comment_updateness_original.csv","r",encoding="utf8") as usersFile:
        #usersFile = open(r"G:\FYP\ModelDataSet.csv","r",encoding="utf8")
        users = pd.read_csv(usersFile,usecols=['Date_feature', 'trending_feature', 'LDA_feature', 'name'])

    df = pd.DataFrame(users)
    # Create x, where x the 'scores' column's values as floats
    x = df[['Date_feature', 'trending_feature', 'LDA_feature']].values.astype(float)
    name = df[['name']].values
    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler()

    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(x)

    # Run the normalizer on the dataframe
    df_normalized = pd.DataFrame(x_scaled)
    dataSet = np.array(df_normalized)

    #users name dataframe
    df_name = pd.DataFrame(name, columns =['name'])
    #features dataframe
    df_post = pd.DataFrame(dataSet, columns =['Date_feature', 'trending_feature', 'LDA_feature'])
    #concat dataframes
    result = pd.concat([df_name, df_post], axis=1, join='inner')
    #print(result)
    df_result = pd.DataFrame(result)

    df_result.to_csv(r'CSV_files\Normalized_features_model_original.csv', mode='a',index=False)