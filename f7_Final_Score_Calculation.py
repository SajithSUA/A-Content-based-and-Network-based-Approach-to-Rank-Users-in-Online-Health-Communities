import pandas as pd
from datetime import date

# called inside self
def removeSameValueInNameList(name):
    namelist = name[:]
    index1 = 0
    for x in namelist:
        index = 0
        while index < len(namelist):
            y = namelist[index]
            if index != index1:
                if y.strip().lower() in x.strip().lower():
                    namelist.pop(index)
                    index -= 1
            index = index + 1
        index1 += 1
    return namelist


# to be passed to the classifier model file
def final_score_calculation_func():
    current_year = int(date.today().year)

    df_info = pd.read_csv('csvPiyu/3_support_scores_predicted_for_comments_with_year_extracted.csv.csv', encoding="utf-8")
    name = df_info['name']
    year = df_info['posted_year']
    info_value = df_info['Info_score']
    emo_value = df_info['Emo_score']

    FinalOut_Infor = []
    FinalOut_Emo = []


    index = 0
    for i in year:
        FinalOut_Infor.append(info_value[index]/(current_year+1-i))
        FinalOut_Emo.append(emo_value[index]/(current_year+1-i))
        index = index+1

    dataFrame = pd.DataFrame(df_info)
    dataFrame['Info_score_By_time'] = FinalOut_Infor
    dataFrame['Emo_score_By_time'] = FinalOut_Emo



    #nameobject list conver to name string list
    name1 = []
    for i in name:
        name1.append(str(i).strip().lower())

    #remove same names in name list
    nameList = removeSameValueInNameList(name1)
    List = []  # all users 216 with info emo scores
    ind = 0
    for i in name1:
        oneList = []  # [[name,infoscore,emoscore],[],[]]
        oneList.append(i)
        oneList.append(FinalOut_Infor[ind])
        oneList.append(FinalOut_Emo[ind])
        List.append(oneList)
        ind = ind+1


    finalOutPut = []
    # print(List)
    for x in nameList:
        oneFinalOut = []  # output of one user
        count_info = 0
        sum_info = 0
        count_emo = 0
        sum_emo = 0
        for y in List:
           if x in y[0]:
               if not y[1] == 0:  # check whether info sup isnt 0, means its an info comment
                   count_info = count_info+1
                   sum_info = sum_info+y[1]
               if not y[2] == 0:
                   count_emo = count_emo+1
                   sum_emo = sum_emo+y[2]
        oneFinalOut.append(x)
        if not count_info == 0:
            oneFinalOut.append(sum_info/count_info)
        if count_info == 0:
            oneFinalOut.append(0)
        if not count_emo == 0:
            oneFinalOut.append(sum_emo/count_emo)
        if count_emo == 0:
            oneFinalOut.append(0)
        finalOutPut.append(oneFinalOut)

    #write Csv
    FinalName = []
    FinalInfoScore = []
    FinalEmoScor = []

    for n in finalOutPut:  # separate by columns, name/info/emo
        FinalName.append(n[0])
        FinalInfoScore.append(n[1])
        FinalEmoScor.append(n[2])

    dataframeFinal = pd.DataFrame()

    dataframeFinal['name']=FinalName
    dataframeFinal['Mean_Info_score'] = FinalInfoScore
    dataframeFinal['Mean_Emo_score'] = FinalEmoScor

    dataFrame.to_csv(r'csvPiyu/4_support_scores_for_comments_with_time_weight.csv', encoding="utf-8")
    dataframeFinal.to_csv(r'csvPiyu/5_final_support_score_by_user.csv', encoding="utf-8")

    print("final scores generated...")















