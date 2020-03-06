from flask import Flask, render_template, flash, request,jsonify
import pandas as pd
import json

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



@app.route('/search', methods=['GET','POST'])
def search():
    print(request)
    print(request.form)
    fl = request.form['search']
    data = pd.read_csv("C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_FeatureSet.csv")
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

        dataset={}

        dataset["name"] = str(name[index])
        dataset["pageRank"]=str(pageRank[index])
        dataset["Hub"] = str(Hub[index])
        dataset["Autho"] = str(Autho[index])
        dataset["Similarity"] = str(Similarity[index])
        dataset["NoOFPost"] = str(NoOFPost[index])
        dataset["length"] = str(length[index])
        dataset["updatness"] = str(updatness[index])
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
    data = pd.read_csv("C:/Users/sajith/PycharmProjects/fyp/datacsv/Final_FeatureSet.csv")
    name = data['Username']
    No_of_post = data['No_of_post']
    dataset = {}
    index = 0
    name1 = []
    No_of_post1 = []
    for i in No_of_post:
        No_of_post1.append(i)
    for i in name:
        name1.append(i)

    dataset["name"] = name1
    dataset["post"] = No_of_post1
    return dataset


if __name__ == '__main__':
    app.run(debug=True)
