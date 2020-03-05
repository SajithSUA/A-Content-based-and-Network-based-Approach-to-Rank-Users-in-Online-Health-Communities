import pandas as pd
import csv
import numpy as np
from fractions import Fraction
import networkx as nx
import matplotlib.pyplot as plt
import os
import datetime

def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def get_no_of_posts(no_of_posts,name,nameList):
    nameAndCommentList = dict()
    count =0
    for i in name:
        nameAndCommentList[i]=no_of_posts[count]
        count=count+1
    print(nameAndCommentList)
    return nameAndCommentList

def calculateSimilarity(name,nameList):
    #create name and comment together
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
    #print(similarityList)

    Final_Similarity_mark_List = dict()
    for x in nameList:
        count = 0
        sum = 0
        for y in similarityList:
            One_Final_Similarity_mark_List =[]
            if x in y[0]:
                sum = sum + y[1]
                count = count + 1
        if not count==0:
            Final_Similarity_mark_List[x]=sum/count
        if count==0:
            Final_Similarity_mark_List[x]=sum/1
    print("Final Similarty Mark List")
    print("---------------------------------------------------------------------------")
    print(Final_Similarity_mark_List)
    return Final_Similarity_mark_List

#remove repeat value in list
def removesamevalueInlist(name) :
    list = name[:]

    index1 = 0
    for x in list:
        index = 0
        while index < len(list):
            y = list[index]
            if index != index1:
                if y.strip().lower() in x.strip().lower():
                    list.pop(index)
                    index -= 1
            index = index + 1
        index1 += 1
    return list

def create_socialNetwork(name,nameCommentMention,nameList):

    indexInnameCommentMention = 0
    for x in nameCommentMention:
        commentInside = x[1]
        for y in nameList:
            if y in str(commentInside).lower():
                if not y in x[0]:
                    if x[2] == 'no':
                        mentioArray = [y]
                        x.pop(2)
                        x.insert(2, mentioArray)
                    elif not y in x[2]:
                        x[2].append(y)

        nameCommentMention.pop(indexInnameCommentMention)
        nameCommentMention.insert(indexInnameCommentMention, x)
        indexInnameCommentMention += 1

    nameAndMention = []
    for x in nameCommentMention:
        onenameAndMention = []
        onenameAndMention.append(x[0])
        onenameAndMention.append(x[2])
        onenameAndMention.append(x[3])
        nameAndMention.append(onenameAndMention)

    with open('datacsv/userConnection.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)

    # reply wala mention karala nathan katada rep kale kiyala ehema ayage reply eka katada kiyala hoyaganima
    # ehema aya reply karanne eyawa mention karala tiyana anthima kenata kiyala api hitanawa

    indexOfnameAndMention = 0
    for x in nameAndMention:
        if x[1] == 'no':
            if not indexOfnameAndMention == 0:
                i = indexOfnameAndMention - 1
                while not i == 0:
                    y = nameAndMention[i]
                    if x[0] in y[1]:
                        update = []
                        update.append(y[0])
                        x.pop(1)
                        x.insert(1, update)
                        nameAndMention.pop(indexOfnameAndMention)
                        nameAndMention.insert(indexOfnameAndMention, x)
                        break
                    i = i - 1

        indexOfnameAndMention += 1

    with open('datacsv/userConnection1.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)

    # user kenek eyage comment eke kenek mention kalla naththan eya ai comment ekak danna kalin eyawa wenakenek mention kalla tiyenam e mention karapu kenata thama comment eka damme kiyala hitanawa

    indexOfnameAndMention = 0
    for x in nameAndMention:
        if x[1] == 'no':
            if not indexOfnameAndMention == 0:
                i = indexOfnameAndMention + 1
                while i < len(nameAndMention):
                    y = nameAndMention[i]
                    if x[0] in y[0]:
                        break
                    else:
                        if x[0] in y[1]:
                            update = []
                            update.append(y[0])
                            x.pop(1)
                            x.insert(1, update)
                            nameAndMention.pop(indexOfnameAndMention)
                            nameAndMention.insert(indexOfnameAndMention, x)
                            break
                    i = i + 1

        indexOfnameAndMention += 1
    with open('datacsv/userConnection2.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)

    # eka digata ekenekgema comment tiyanakota palaweni eke mention kalla dewani eke mention kalla nathan kawawath e comment ekath palaweni kenatama kiyala hitanawa

    indexOfnameAndMention = 0
    for x in nameAndMention:
        if x[1] == 'no':
            if not indexOfnameAndMention == 0:
                i = indexOfnameAndMention - 1
                y = nameAndMention[i]
                if x[0] in y[1]:
                    update = []
                    update.append(y[0])
                    x.pop(1)
                    x.insert(1, update)
                    nameAndMention.pop(indexOfnameAndMention)
                    nameAndMention.insert(indexOfnameAndMention, x)
        indexOfnameAndMention += 1
    with open('datacsv/userConnection3.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)

    # danatamath mention kenek nathi original poster nowena aya comment eka dala tiyenne initial post ekata kiyala hitala e ayage mention karapu kene original poster karanawa
    indexOfnameAndMention = 0
    originalPoster = nameAndMention[0][0]
    for x in nameAndMention:
        if x[2]==0:
            originalPoster=x[0]
        if x[1] == 'no' and x[0] != originalPoster:
            update = []
            update.append(originalPoster)
            x.pop(1)
            x.insert(1, update)
            nameAndMention.pop(indexOfnameAndMention)
            nameAndMention.insert(indexOfnameAndMention, x)
        indexOfnameAndMention += 1

    with open('datacsv/userConnection4.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)
    csvFile.close()

    # create social network
    # we create final social network using "nameAndMention" array
    # first we get name List(only users in 1 tread)
    # next we check 1 elemnt eka nameAndMention eke first element eke saha nameList eke ituru eliment eka mention names wala inna count eka

    # FinalsocialNetwork =[]
    # for oneName1 in nameList:
    #     oneFinalsocialNetwork = []
    #     oneFinalsocialNetwork.append(oneName1)
    #     for x in nameAndMention:
    #         if oneName1==x[0]:
    #             for oneName2 in nameList:
    #                 count=0
    #                 for x1 in nameAndMention:
    #                     if oneName1==x1[0] and oneName2 in x1[1]:
    #                         count=count+1
    #                 oneFinalsocialNetwork.append(count)
    #     FinalsocialNetwork.append(oneFinalsocialNetwork)
    #
    # print(FinalsocialNetwork)


    #original poster ge comment wala kawawath mention wela nathan
    index=0
    originalPoster = nameAndMention[0][0]
    for i in nameAndMention:
        if i[2]==0:
            originalPoster=i[0]
        if i[1] == 'no' and i[0] == originalPoster and i[2]!=0:
            mentionName=[]
            for y in range(index-1,-1,-1):
                if nameAndMention[y][0]==originalPoster:
                    break
                elif originalPoster in nameAndMention[y][1]:
                    mentionName.append(nameAndMention[y][0])
            if len(mentionName)!=0:
                i.pop(1)
                i.insert(1, mentionName)
                nameAndMention.pop(index)
                nameAndMention.insert(index,i)
        index=index+1

    with open('datacsv/userConnection5.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,mention name\n")
        writer = csv.writer(csvFile)
        writer.writerows(nameAndMention)
    csvFile.close()


    FinalsocialNetwork = []
    for oneName1 in nameList:
        oneFinalsocialNetwork = []
        oneFinalsocialNetwork.append(oneName1)
        for oneName2 in nameList:
            count = 0
            for x in nameAndMention:
                if oneName1 in x[0] and oneName2 in x[1]:
                    count = count + 1
            oneFinalsocialNetwork.append(count)
        FinalsocialNetwork.append(oneFinalsocialNetwork)
    print("")
    print("")
    print("")
    print(
        "-------------------------------------------- name and mentions name in form --------------------------------------------")
    print(nameAndMention)
    print("")
    print("")
    print("")
    print(
        "-------------------------------------------- Social network array --------------------------------------------")
    print(FinalsocialNetwork)

    # social network print

    with open('datacsv/socialNetwork.csv', 'a', newline='') as csvFile:
        a = "name"
        for name in nameList:
            a = a + "," + name
        a = a + "\n"
        print
        csvFile.write(a)
        writer = csv.writer(csvFile)
        writer.writerows(FinalsocialNetwork)
    csvFile.close()
    return FinalsocialNetwork

def pageRank_Algo(FinalsocialNetwork):

    # create page rank social network array
    array = []
    for x in FinalsocialNetwork:
        count = 0
        onearray = []
        nu = 0
        for y in x:
            if not nu == 0:
                if int(y) > 0:
                    count = count + 1
            nu = nu + 1
        nu1 = 0
        for t in x:
            if not nu1 == 0:
                if int(t) > 0:
                    onearray.append(1 / count)
                else:
                    onearray.append(0)
            nu1 = nu1 + 1
        array.append(onearray)
    r1 = np.matrix(array)
    print("")
    print("")
    print("")
    print(
        "-------------------------------------------- Page rank input metrix --------------------------------------------")
    print(r1)
    Mat = np.transpose(r1)
    print(Mat)

    # Page rank algorithem

    def display_format(my_vector, my_decimal):
        return np.round((my_vector).astype(np.float), decimals=my_decimal)

    my_dp = Fraction(1, len(nameList))

    print(my_dp)
    Ex = np.zeros((len(nameList), len(nameList)))

    Ex[:] = my_dp

    beta = .85
    Al = beta * Mat + ((1 - beta) * Ex)
    array = []
    for i in nameList:
        array.append(my_dp)
    r = np.matrix(array)
    r = np.transpose(r)

    previous_r = r
    for i in range(1, 100):
        r = Al * r
        if (previous_r == r).all():
            break
        previous_r = r
    print("")
    print("")
    print("")
    print("-------------------------------------------- page rank value --------------------------------------------")
    print("Final:\n", display_format(r, 3))
    print("sum", np.sum(r))
    Final_page_Rank_value = dict()
    ind=0
    for l in nameList:
        Final_page_Rank_value[l]=r.item(ind)
        ind=ind+1
    return Final_page_Rank_value

def pageRank_Score_print(r):
    with open('datacsv/PageRankScore.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,Page Rank score \n")
        writer = csv.writer(csvFile)
        writer.writerows(r)
    csvFile.close()

def Hits_algorithem(FinalsocialNetwork,nameList):
    G = nx.DiGraph()
    for x in FinalsocialNetwork:
        index =0
        for y in x:
            if not index==0:
                if int(y)>0:
                    G.add_edges_from([(x[0],nameList[index-1])])
            index=index+1

    plt.figure(figsize=(100, 100))
    nx.draw_networkx(G, with_labels=True)
    #plt.show()


    hubs, authorities = nx.hits(G, max_iter= 50000000, normalized=True)
# page rank value genarate in nx library
    pr = nx.pagerank(G, alpha=0.85)

    # The in-built hits function returns two dictionaries keyed by nodes
    # containing hub scores and authority scores respectively.

    print("Hub Scores: ", hubs)
    for x in nameList:
        print(x ,":" , hubs.get(x))
    print("authorities Scores: ", authorities)
    for y in nameList:
        print(y, ":", authorities .get(y))

    return hubs,authorities,pr

def Print_final_featuers(nameList,Page_Rank_Result,Final_hubs,Final_authorities,Similarity_Result,Final_Number_Of_post_Count,pr,actual_NoOf_Post,length_in_comment,averge_updatness):

    allDataArray=[]
    for oneName in nameList:
        DataArray = []
        DataArray.append(oneName)
        DataArray.append(Page_Rank_Result.get(oneName))
        DataArray.append(Final_hubs.get(oneName))
        DataArray.append(Final_authorities.get(oneName))
        DataArray.append(Similarity_Result.get(oneName))
        DataArray.append(Final_Number_Of_post_Count.get(oneName))
       #DataArray.append(pr.get(oneName))
       #DataArray.append(actual_NoOf_Post.get(oneName))
        DataArray.append(length_in_comment.get(oneName))
        DataArray.append(averge_updatness.get(oneName))
        allDataArray.append(DataArray)

    with open('datacsv/Final_FeatureSet.csv', 'a', newline='') as csvFile:
        csvFile.write("Username,Page_Rank,Hub,Authority,Similarity,No_of_post,length_in_comment,updatness\n")
        writer = csv.writer(csvFile)
        writer.writerows(allDataArray)
    csvFile.close()

def actualNumberOfPost(name,nameList):
    nameAndNumberOfPost= dict()
    for oneName in nameList:
        count=0
        for x in name:
            if oneName in x:
                count=count+1
        nameAndNumberOfPost[oneName]=count
    return nameAndNumberOfPost

def get_average_coment_Length(nameCommentMention,nameList):
    length_in_comment=[]
    for x in nameCommentMention:
        one_length_in_comment=[]
        one_length_in_comment.append(x[0])
        one_length_in_comment.append(len(x[1].replace(' ', '')))
        length_in_comment.append(one_length_in_comment)
    average_length_in_comment = dict()
    for y in nameList:
        count=0
        sum=0
        for i in length_in_comment:
            if y in i[0]:
                sum=sum+i[1]
                count=count+1
        if not count==0:
            average_length_in_comment[y]=sum/count
        else:
            average_length_in_comment[y] = 0
    return average_length_in_comment

def get_average_updatness():
    data = pd.read_csv("C:/Users/sajith/PycharmProjects/fyp/datacsv/nuwanoutput/Final_result.csv")
    name_Without_Clear = data['Name']
    updatness = data['Predicted']
    name=[]
    for x in name_Without_Clear:
        name.append(str(x).replace('…', '').strip().lower())
    name_and_Updatness=[]
    index=0
    for i in name:
        oneName_and_updatness=[]
        oneName_and_updatness.append(i)
        oneName_and_updatness.append(updatness[index])
        name_and_Updatness.append(oneName_and_updatness)
        index=index+1

    average_updatnes= dict()
    for y in nameList:
        count=0
        sum=0
        for i in name_and_Updatness:
            if y in i[0]:
                sum=sum+i[1]
                count=count+1
        if not count==0:
            average_updatnes[y]=sum/count
        else:
            average_updatnes[y] = 0
    return average_updatnes

def remove_existing_CSV():
    files="C:/Users/sajith/PycharmProjects/fyp/datacsv"
    for file1 in os.listdir(files):
        if file1.endswith('.csv'):
            os.remove(files + '/' + file1)


# add data set
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/merged csvs data.csv")
name_Without_Clear = data['name']
comment = data['comment']
post_id = data['id']
no_of_posts = data['no_of_posts']

name = []

# remove "..." characters in name field and convert to lower case in string and strip

for x in name_Without_Clear:
    name.append(str(x).replace('…', '').strip().lower())
nameCommentMention = []
index = 0
for x in name:
    oneNameCommentMention = []
    oneNameCommentMention.append(str(x))
    oneNameCommentMention.append(comment[index])
    oneNameCommentMention.append('no')
    oneNameCommentMention.append(post_id[index])
    nameCommentMention.append(oneNameCommentMention)
    index += 1

nameList= removesamevalueInlist(name)


remove_existing_CSV()

a = datetime.datetime.now()

Final_Number_Of_post_Count=get_no_of_posts(no_of_posts,name,nameList)

b = datetime.datetime.now()

FinalsocialNetwork=create_socialNetwork(name,nameCommentMention,nameList)

c = datetime.datetime.now()

Page_Rank_Result=pageRank_Algo(FinalsocialNetwork)

d = datetime.datetime.now()

Final_hubs,Final_authorities,pr=Hits_algorithem(FinalsocialNetwork,nameList)

e = datetime.datetime.now()

Similarity_Result=calculateSimilarity(name,nameList)

f = datetime.datetime.now()

actual_NoOf_Post=actualNumberOfPost(name,nameList)

g = datetime.datetime.now()

length_in_comment=get_average_coment_Length(nameCommentMention,nameList)

h = datetime.datetime.now()

averge_updatness=get_average_updatness()

i = datetime.datetime.now()

Print_final_featuers(nameList,Page_Rank_Result,Final_hubs,Final_authorities,Similarity_Result,Final_Number_Of_post_Count,pr,actual_NoOf_Post,length_in_comment,averge_updatness)

j = datetime.datetime.now()


print("print",j-i)
print("updatness",i-h)
print("length",h-g)
print("actual no post", g-f)
print("similarity",f-e)
print("hits",e-d)
print("page rank",d-c)
print("socia net",c-b)
print("no of post",b-a)


