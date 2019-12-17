import pandas as pd
import csv

#remove repeat value in list
def removesamevalueInlist(list) :
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



#add data set
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Anxiety.csv")
name1= data['name']
comment=data['comment']
#print (name1)
name=[]

# remove "â€¦" characters in name field and convert to lower case in string and strip

for x in name1:
    name.append(str(x).replace('…', '').strip().lower())

originalPoster=name[0]

nameCommentMention=[]

index=0
for x in name:
    oneNameCommentMention=[]
    oneNameCommentMention.append(str(x))
    oneNameCommentMention.append(comment[index])
    oneNameCommentMention.append('no')
    nameCommentMention.append(oneNameCommentMention)
    index+=1

#print(len(nameCommentMention))

nameList= removesamevalueInlist(name)
#print(len(nameList))

# with open('person1.csv', 'a', newline='') as q:
#     for x in nameList:
#      q.write(x+"\n")

#print(nameCommentMention)

indexInnameCommentMention=0
for x in nameCommentMention:
    commentInside=x[1]
    for y in nameList:
        if y in str(commentInside).lower():
            if not y in x[0]:
                if x[2]=='no':
                    mentioArray=[y]
                    x.insert(2,mentioArray)
                elif not y in x[2]:
                        x[2].append(y)


    nameCommentMention.pop(indexInnameCommentMention)
    nameCommentMention.insert(indexInnameCommentMention,x)
    indexInnameCommentMention +=1







nameAndMention=[]
for x in nameCommentMention:
    onenameAndMention=[]
    onenameAndMention.append(x[0])
    onenameAndMention.append(x[2])
    nameAndMention.append(onenameAndMention)

with open('userConnection.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)

#reply wala mention karala nathan katada rep kale kiyala ehema ayage reply eka katada kiyala hoyaganima
#ehema aya reply karanne eyawa mention karala tiyana anthima kenata kiyala api hitanawa

indexOfnameAndMention=0
for x in nameAndMention:
    if x[1]=='no':
        if not indexOfnameAndMention==0:
            i=indexOfnameAndMention-1
            while not i==0:
                y=nameAndMention[i]
                if x[0] in y[1]:
                  update=[]
                  update.append(y[0])
                  x.pop(1)
                  x.insert(1,update)
                  nameAndMention.pop(indexOfnameAndMention)
                  nameAndMention.insert(indexOfnameAndMention,x)
                  break
                i=i-1

    indexOfnameAndMention+=1


with open('userConnection1.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)


#user kenek eyage comment eke kenek mention kalla naththan eya ai comment ekak danna kalin eyawa wenakenek mention kalla tiyenam e mention karapu kenata thama comment eka damme kiyala hitanawa

indexOfnameAndMention=0
for x in nameAndMention:
    if x[1]=='no':
        if not indexOfnameAndMention==0:
            i=indexOfnameAndMention+1
            while i<len(nameAndMention):
                y=nameAndMention[i]
                if x[0] in y[0]:
                    break
                else:
                    if x[0] in y[1]:
                      update=[]
                      update.append(y[0])
                      x.pop(1)
                      x.insert(1,update)
                      nameAndMention.pop(indexOfnameAndMention)
                      nameAndMention.insert(indexOfnameAndMention,x)
                      break
                i=i+1

    indexOfnameAndMention+=1
with open('userConnection2.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)

#eka digata ekenekgema comment tiyanakota palaweni eke mention kalla dewani eke mention kalla nathan kawawath e comment ekath palaweni kenatama kiyala hitanawa

indexOfnameAndMention=0
for x in nameAndMention:
    if x[1]=='no':
        if not indexOfnameAndMention==0:
            i=indexOfnameAndMention-1
            y=nameAndMention[i]
            if x[0] in y[1]:
                      update=[]
                      update.append(y[0])
                      x.pop(1)
                      x.insert(1,update)
                      nameAndMention.pop(indexOfnameAndMention)
                      nameAndMention.insert(indexOfnameAndMention,x)
    indexOfnameAndMention += 1
with open('userConnection3.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)

# danatamath mention kenek nathi original poster nowena aya comment eka dala tiyenne initial post ekata kiyala hitala e ayage mention karapu kene original poster karanawa
indexOfnameAndMention=0
for x in nameAndMention:
    if x[1]=='no' and x[0]!=originalPoster :
        update = []
        update.append(originalPoster)
        x.pop(1)
        x.insert(1, update)
        nameAndMention.pop(indexOfnameAndMention)
        nameAndMention.insert(indexOfnameAndMention, x)
    indexOfnameAndMention += 1

with open('userConnection4.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)
csvFile.close()


# create social network
# we create final social network using "nameAndMention" array
#first we get name List(only users in 1 tread)
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


FinalsocialNetwork =[]
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
print("-------------------------------------------- name and mentions name in form --------------------------------------------")
print(nameAndMention)
print("")
print("")
print("")
print("-------------------------------------------- Social network array --------------------------------------------")
print(FinalsocialNetwork)


#social network print

with open('socialNetwork.csv', 'a', newline='') as csvFile:
    a="name"
    for name in nameList:
        a=a+","+name
    a=a+"\n"
    print
    csvFile.write(a)
    writer = csv.writer(csvFile)
    writer.writerows(FinalsocialNetwork)
csvFile.close()



#create page rank social network array

import numpy as np
import scipy as sc
import pandas as pd
from fractions import Fraction


array=[]
for x in FinalsocialNetwork:
    count=0
    onearray=[]
    nu=0
    for y in x:
        if not nu==0:
            if int(y)>0:
                count=count+1
        nu=nu+1
    nu1=0
    for t in x:
        if not nu1 == 0:
            if int(t)>0:
                onearray.append(1/count)
            else:
                onearray.append(0)
        nu1=nu1+1
    array.append(onearray)



r1=np.matrix(array)
print("")
print("")
print("")
print("-------------------------------------------- Page rank input metrix --------------------------------------------")
print(r1)
Mat = np.transpose(r1)
print(Mat)

#Page rank algorithem

def display_format(my_vector, my_decimal):
   return np.round((my_vector).astype(np.float), decimals=my_decimal)
my_dp = Fraction(1,len(nameList))


print(my_dp)
# Mat = np.matrix([[0,0,1],
#         [1/2,0,0],
#         [1/2,1,0]])
Ex = np.zeros((len(nameList),len(nameList)))

Ex[:] = my_dp


beta = 0.8
Al = beta * Mat + ((1-beta) * Ex)
array=[]
for i in nameList:
    array.append(my_dp)
r = np.matrix(array)
r = np.transpose(r)

previous_r = r
for i in range(1,100):
   r = Al * r
   #print (display_format(r,3))
   if (previous_r==r).all():
      break
   previous_r = r
print("")
print("")
print("")
print("-------------------------------------------- page rank value --------------------------------------------")
print ("Final:\n", display_format(r,3))
print ("sum", np.sum(r))



#page rank marks in users
allArray=[]

count2=0
for q in nameList:
    array1 = []
    array1.append(q)
    array1.append(r.item(count2))
    allArray.append(array1)
    count2=count2+1

with open('PageRankScore.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Page Rank score \n")
    writer = csv.writer(csvFile)
    writer.writerows(allArray)
csvFile.close()





