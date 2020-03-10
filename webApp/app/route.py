from flask import Flask, render_template, flash, request,jsonify
import pandas as pd
import json
#data csv file path

a="C:/Users/sajith/PycharmProjects/fyp/datacsv/UI/Final_FeatureSet.csv"
b="C:/Users/sajith/PycharmProjects/fyp/datacsv/UI/normalize.csv"
c='C:/Users/sajith/PycharmProjects/fyp/datacsv/UI/Final_result_withRank.csv'

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ranking', methods=['GET','POST'])
def addProduct():
    dataset=createDataInRanking()
    dataset["erro"] = False
    json_dump = json.dumps(dataset)
    return render_template('ranking.html',dataset=json_dump)


@app.route('/expert', methods=['GET','POST'])
def getExpert():
    dataset1=get_users_Wice_Category('intermediate Users', 'Novice Users')
    dataset1["erro"] = False

    json_dump1 = json.dumps(dataset1)
    return render_template('expertUsers.html',dataset1=json_dump1)


@app.route('/novice', methods=['GET','POST'])
def getNovice():
    dataset1=get_users_Wice_Category('intermediate Users', 'Expert Users')
    dataset1["erro"] = False

    json_dump1 = json.dumps(dataset1)
    return render_template('NoviceUsers.html',dataset1=json_dump1)


@app.route('/intermediate', methods=['GET','POST'])
def getIntermediate():
    dataset1=get_users_Wice_Category('Novice Users', 'Expert Users')
    dataset1["erro"] = False

    json_dump1 = json.dumps(dataset1)
    return render_template('intermediate.html',dataset1=json_dump1)




@app.route('/search', methods=['GET','POST'])
def search():
    print(request)
    print(request.form)
    fl = request.form['search']
    data = pd.read_csv(b)
    datasetUSerRank=pd.read_csv(c)
    name = data['Username']
    index=0
    match=False
    for i in name:
        if fl == i:
            match=True
            break
        index=index+1
    print (match)
    if match:
        pageRank = data['Page_Rank']
        Hub = data['Hub']
        Autho = data['Authority']
        Similarity = data['Similarity']
        NoOFPost = data['No_of_post']
        length = data['length_in_comment']
        updatness = data['updatness']
        Info_Support= data['Info_Score']
        Emo_Support=data['Emo_Score']
        userRank=datasetUSerRank['Predicted Rank']
        userCategory=datasetUSerRank['User_category']

        dataset={}

        dataset["name"] = str(name[index])
        dataset["pageRank"]=str(format((pageRank[index]/1)*100,'.2f'))+"%"
        dataset["Hub"] = str(format((Hub[index]/1)*100,'.2f'))+"%"
        dataset["Autho"] = str(format((Autho[index]/1)*100,'.2f'))+"%"
        dataset["Similarity"] = str(format((Similarity[index]/1)*100,'.2f'))+"%"
        dataset["NoOFPost"] = str(format((NoOFPost[index]/1)*100,'.2f'))+"%"
        dataset["length"] = str(format((length[index]/1)*100,'.2f'))+"%"
        dataset["updatness"] = str(format((updatness[index]/1)*100,'.2f'))+"%"
        dataset["Info_Score"]=str(format((Info_Support[index]/1)*100,'.2f'))+"%"
        dataset["Emo_Score"]=str(format((Emo_Support[index]/1)*100,'.2f'))+"%"

        dataset["userRank"]=str(format(userRank[index],'.0f'))
        dataset["userCategory"]=str(userCategory[index])
        json_dump1 = json.dumps(dataset)
        print(json_dump1)

        return render_template('addProduct.html', datset=json_dump1)
    else:
        dataset = createDataInRanking()
        dataset["erro"] = True
        json_dump = json.dumps(dataset)

        return render_template('ranking.html',dataset=json_dump)




@app.route('/test', methods=['GET', 'POST'])
def test():
    # selectedProduct = request.get_json()
    return {
        "username" : "milanda",
        "telephoneNo" : "0715864650",
        "age":"15",
        "height" :  "10",
        "weight" : "10"
    }

def createDataInRanking():
    data = pd.read_csv(c)
    dataFrame=pd.DataFrame(data)
    dataFrame1=dataFrame.sort_values(by=['Predicted Rank'])
    UserRank=dataFrame1.get('Predicted Rank')
    name=dataFrame1.get('Username')
    dataset = {}
    index = 0
    name1 = []
    No_of_post1 = []
    for i in UserRank:
        No_of_post1.append(str(round(int(i))))
    for i in name:
        name1.append(i)

    dataset["name"] = name1
    dataset["post"] = No_of_post1
    return dataset

def get_users_Wice_Category(name1,name2):
    data1 = pd.read_csv(c)

    dataframe = pd.DataFrame(data1)

    data = dataframe.sort_values(by=['Predicted_MLR'], ascending=False)

    data2 = data[data.User_category != name1]

    data3 = data2[data2.User_category != name2]

    User_type_name = 'Expert Users'
    name = data3.get('Username')
    Score = data3.get('Predicted_MLR')
    type = data3.get('User_category')
    dataset1 = {}
    name1 = []
    Score1 = []
    for i in name:
        name1.append(i)
    for x in Score:
        Score1.append(str(format(x,'.2f')))

    dataset1["name"] = name1
    dataset1["post"] = Score1
    return dataset1

if __name__ == '__main__':
    app.run(debug=True)
