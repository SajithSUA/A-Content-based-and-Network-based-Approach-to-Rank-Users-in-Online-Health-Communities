import numpy as np
import pandas as pd
from sklearn import preprocessing

def normalization():
    usersFile = open('C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_FeatureSet.csv', 'r', encoding="utf-8")
    users = pd.read_csv(usersFile,usecols=['Username','Page_Rank','Hub','Authority','Similarity','No_of_post','length_in_comment','updatness'])
    name=users['Username']
    print (name)
    df = pd.DataFrame(users)
    # Create x, where x the 'scores' column's values as floats
    x = df[['Page_Rank','Hub','Authority','Similarity','No_of_post','length_in_comment','updatness']].values.astype(float)

    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler()

    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(x)

    # Run the normalizer on the dataframe
    df_normalized = pd.DataFrame(x_scaled)
    df_normalized['Username']=name
    print(df_normalized)

    dataSet = np.array(df_normalized)

    df_post = pd.DataFrame(dataSet, columns=['Page_Rank','Hub','Authority','Similarity','No_of_post','length_in_comment','updatness','Username'])
    df_post.to_csv(r'C:/Users/sajith/PycharmProjects/fyp/datacsv/normalize.csv', mode='a',index=False)