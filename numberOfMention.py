import pandas as pd
import csv
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Thickening near armpit and prominent veins, heaviness.csv")
name1= data['name']
numberOfpost=data['no_of_posts']
name=[]


# remove "â€¦" characters in name field and convert to lower case in string and strip

for x in name1:
    name.append(str(x).replace('…', '').strip().lower())



comment=data['comment']

nameArrayLength=len(name)
commentArrayLangth=len(comment)

if nameArrayLength==commentArrayLangth:
    NameAndMenCount=[]
    indexinArray = 0
    for x in name:
        a=0;
        oneNameAndMenCount = []
        indexOfCommentArray = 0
        for y in comment:
            # remove own comment mentions count
            if not x in name[indexOfCommentArray]:


                if str(x).lower().replace('…', '') in str(y).lower():
                    a=a+1
            indexOfCommentArray=indexOfCommentArray+1

        oneNameAndMenCount.append(x.replace('…', '').strip())
        oneNameAndMenCount.append(a)
        oneNameAndMenCount.append(numberOfpost[indexinArray])
        NameAndMenCount.append(oneNameAndMenCount)
        indexinArray = indexinArray + 1


#delete repeated users

    index1=0
    print(NameAndMenCount)
    for x in NameAndMenCount:
        index=0
        while index<len(NameAndMenCount):
            y=NameAndMenCount[index]
            if  index!=index1:
                if x[0] in y[0]:
                    NameAndMenCount.pop(index)
                    index-=1
            index=index+1
        index1=index1+1
    print(NameAndMenCount)


#write csv file
with open('person.csv', 'a', newline='') as csvFile:
    csvFile.write("Username,Mention count,Number Of post\n")
    writer = csv.writer(csvFile)
    writer.writerows(NameAndMenCount)
    writer.writerows(NameAndMenCount)

csvFile.close()