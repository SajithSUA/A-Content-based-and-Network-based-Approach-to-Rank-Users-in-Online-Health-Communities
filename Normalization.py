import numpy as np
import pandas as pd
from sklearn import preprocessing
usersFile = open('C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_FeatureSet.csv', 'r', encoding="utf-8")
users = pd.read_csv(usersFile,usecols=['Page_Rank','Hub','Authority','Similarity','No_of_post','pr','actual_NoOf_Post'])

df = pd.DataFrame(users)
# Create x, where x the 'scores' column's values as floats
x = df[['Page_Rank','Hub','Authority','Similarity','No_of_post','pr','actual_NoOf_Post']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
print(df_normalized)

dataSet = np.array(df_normalized)

df_post = pd.DataFrame(dataSet, columns=['Page_Rank','Hub','Authority','Similarity','No_of_post','pr','actual_NoOf_Post'])
df_post.to_csv(r'C:/Users/sajith/PycharmProjects/fyp/datacsv/normalize.csv', mode='a',
               index=False)