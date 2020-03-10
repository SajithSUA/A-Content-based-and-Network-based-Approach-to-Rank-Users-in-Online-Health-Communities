import pandas as pd
import csv
data = pd.read_csv("C:/Users/sajith/Desktop/project/data set/Worried I'm overreacting.csv")
print(data)

name= data['name']
print(name)
noOfrep=name
#name.to_csv("new.csv")


csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('person.csv', 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(name)


csvFile.close()