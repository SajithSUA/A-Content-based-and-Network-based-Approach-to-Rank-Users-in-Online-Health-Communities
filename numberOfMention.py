import pandas as pd
import csv
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Interpreting Mammograms- Architectural Distortion.csv")
name= data['name']
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
            if not x==name[indexOfCommentArray]:

                # remove "â€¦" characters in name field and convert to lower case in string
                if x.lower().replace('…', '') in y.lower():
                    a=a+1
            indexOfCommentArray=indexOfCommentArray+1
        oneNameAndMenCount.append(x.replace('…', ''))
        oneNameAndMenCount.append(a)
        NameAndMenCount.append(oneNameAndMenCount)
        #print(oneNameAndMenCount)
        #print(x.replace('…', '')+"-",a)

    print(NameAndMenCount)

# csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('person.csv', 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(NameAndMenCount)


csvFile.close()