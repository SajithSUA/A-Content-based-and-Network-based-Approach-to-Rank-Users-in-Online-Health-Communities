import numpy as np
import pandas as pd
from sklearn import preprocessing
usersFile = open('C:/Users/sajith/PycharmProjects/fyp/Final_FeatureSet.csv', 'r', encoding="utf-8")
users = pd.read_csv(usersFile,usecols=['Page Rank score', 'Hub Score', ' Authority Score', 'Similarity Score', 'No of post '])

df = pd.DataFrame(users)
# Create x, where x the 'scores' column's values as floats
x = df[['Page Rank score', 'Hub Score', ' Authority Score', 'Similarity Score', 'No of post ']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
print(df_normalized)

posts_array = np.array(df_normalized)
print(posts_array)
df_users = pd.DataFrame(posts_array,
                        columns=['Page Rank score', 'Hub Score', ' Authority Score', 'Similarity Score', 'No of post '])
df_users.to_csv(r'C:/Users/sajith/PycharmProjects/fyp/normalize.csv', mode='a',
                index=False)