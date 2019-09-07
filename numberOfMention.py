import pandas as pd
import csv
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Anxiety.csv")
name1= data['name']
name=[]


# remove "â€¦" characters in name field and convert to lower case in string and strip

for x in name1:
    name.append(str(x).replace('…', '').strip().lower())



comment=data['comment']

nameArrayLength=len(name)
commentArrayLangth=len(comment)

if nameArrayLength==commentArrayLangth:
    NameAndMenCount=[]
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
        NameAndMenCount.append(oneNameAndMenCount)
        #print(oneNameAndMenCount)
        #print(x.replace('…', '')+"-",a)



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



with open('person.csv', 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(NameAndMenCount)


csvFile.close()