import pandas as pd
import csv
import numpy as np
def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def calculateSimilarity(name):
    # create comment and name together
    nameCommentCombined = []
    ind = 0
    for e in name:
        nameCommentCombinedOne = []
        nameCommentCombinedOne.append(e)
        nameCommentCombinedOne.append(str(comment[ind]).replace('"', ''))
        nameCommentCombined.append(nameCommentCombinedOne)
        ind = ind + 1

    index=0
    similarityList = []
    for x in nameCommentCombined:
        One_similarityList=[]
        Final_OneComment_Similarity_Scor=0
        for e in range(0,index+1):
            y=nameCommentCombined[e]
            if not x[0] in y[0]:
                similarityScore = get_jaccard_sim(x[1], y[1])
                if Final_OneComment_Similarity_Scor<similarityScore:
                    Final_OneComment_Similarity_Scor=similarityScore
        One_similarityList.append(x[0])
        One_similarityList.append(Final_OneComment_Similarity_Scor)
        similarityList.append(One_similarityList)
        index=index+1
    print(similarityList)


#add data set
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/MRI Question.csv")
name1= data['name']
comment=data['comment']
name=[]
for x in name1:
    name.append(str(x).replace('…', '').strip().lower())
print(len(name))


calculateSimilarity(name)
