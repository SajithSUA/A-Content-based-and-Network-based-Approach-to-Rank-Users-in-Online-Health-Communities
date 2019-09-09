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
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Worried I'm overreacting.csv")
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

print(len(nameCommentMention))

nameList= removesamevalueInlist(name)
print(len(nameList))

# with open('person1.csv', 'a', newline='') as q:
#     for x in nameList:
#      q.write(x+"\n")

print(nameCommentMention)

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

with open('person.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Comment,mention name\n")
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


with open('person1.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Comment,mention name\n")
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
                      update.append("123"+y[0])
                      x.pop(1)
                      x.insert(1,update)
                      nameAndMention.pop(indexOfnameAndMention)
                      nameAndMention.insert(indexOfnameAndMention,x)
                      break
                i=i+1

    indexOfnameAndMention+=1
with open('person2.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Comment,mention name\n")
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
                      update.append("456"+y[0])
                      x.pop(1)
                      x.insert(1,update)
                      nameAndMention.pop(indexOfnameAndMention)
                      nameAndMention.insert(indexOfnameAndMention,x)

with open('person3.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Comment,mention name\n")
    writer = csv.writer(csvFile)
    writer.writerows(nameAndMention)

# danatamath mention kenek nathi original poster nowena aya comment eka dala tiyenne initial post ekata kiyala hitala e ayage mention karapu kene original poster karanawa

csvFile.close()








