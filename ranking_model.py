import pandas as pd
import numpy as np
def categorizeUsers(score):
    bins=np.linspace(min(score),max(score),4)
    print(bins)
    group_names=['Novice Users','intermediate Users','Expert Users']
    User_category=pd.cut(score,bins,labels=group_names,include_lowest=True)
    print(User_category)
    return User_category

def rank_scores():
    dataset = 'C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_result.csv'
    score = pd.read_csv(dataset)

    answerDetails = score[['Username']]
    print(answerDetails)

    # convert score array into dataframe
    score_df = pd.DataFrame(score['Predicted_MLR'], columns=['Predicted_MLR'])
    print(score_df)
    # create rank column
    score_df['Predicted Rank'] = score_df['Predicted_MLR'].rank(ascending=False)

    # merging 2 dataframes to display
    score_df.reset_index(drop=True, inplace=True)
    answerDetails.reset_index(drop=True, inplace=True)
    resultsList = pd.concat([score_df, answerDetails], axis=1)
    print('===============Random Forest Regression Model-Predicted Rank List==============')
    User_category=categorizeUsers(score['Predicted_MLR'])
    resultsList['User_category']=User_category
    print(resultsList)
    resultsList.to_csv(r'C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_result_withRank.csv',mode='a',index=False)



