# load and evaluate a saved model
from tensorflow.keras.models import load_model
import pandas as pd
from tensorflow.keras.preprocessing import sequence
import pickle
import f5_Regression_Models as regression_model
import f6_Extaract_Year as extract_year
import f7_Final_Score_Calculation as final_score


df = pd.read_csv('C:/Users/sajith/Desktop/project/data set/project_dataset.csv', delimiter=',', encoding='utf-8')

# load model
model = load_model('RNN_Model.h5')

# summarize model.
print(model.summary())

with open('tokenizer.pickle', 'rb') as handle:
        tok = pickle.load(handle)

##########################################
# sample_texts_pos = ["WC3 They missed my cancer on both the mammogram and ultrasound but I had extremely dense breasts. If you have fatty breasts then the mammogram is less likely to miss IDC but may still miss ILC. Maybe someone more familiar with that can chime in but if an MRI would give you peace of mind then I don't think it unreasonable for you to request one. Personally I think baseline breast MRIs should be standard."]
# sample_texts_neg = ["So glad to hear that Epic...I have been down that road before and it really does help. I think it takes a lot of courage to make that first appointment and go but it helps so much. :-)"]
#
# txts = tok.texts_to_sequences(sample_texts_pos)
# txts = sequence.pad_sequences(txts, maxlen=max_len)
# preds = model.predict(txts)
# print(preds[0][0])
#
# txts = tok.texts_to_sequences(sample_texts_neg)
# txts = sequence.pad_sequences(txts, maxlen=max_len)
# preds = model.predict(txts)
# print(preds[0][0])
##########################

info_comments, info_names, info_times = ([] for i in range(3))
emo_comments, emo_names, emo_times = ([] for i in range(3))


for index, row in df.iterrows():
    texts = tok.texts_to_sequences([row['comment']])
    texts = sequence.pad_sequences(texts, maxlen=500)
    preds = model.predict(texts)

    if float(preds[0][0]) < 0.5: #predict value i 0 0 index
        info_comments.append(row['comment'])
        info_names.append(row['name'])
        info_times.append(row['posted_time'])
    else:
        emo_comments.append(row['comment'])
        emo_names.append(row['name'])
        emo_times.append(row['posted_time'])


dataset_info_data = {'comment': info_comments,
                     'name': info_names,
                     'posted_time': info_times}

dataset_emo_data = {'comment': emo_comments,
                    'name': emo_names,
                    'posted_time': emo_times}

dataset_info = [dataset_info_data] #to make it an array
dataset_emo = [dataset_emo_data]

column_names = ["comment", "name", "posted_time"]
header = True

for dataset1 in dataset_info:
    df_i = pd.DataFrame(dataset1)
    df_i = df_i[column_names]
    mode = 'w' if header else 'a'
    df_i.to_csv('csvPiyu/1.1_emo_classified.csv', encoding='utf-8', mode=mode, header=True, index=False)

for dataset2 in dataset_emo:
    df_e = pd.DataFrame(dataset2)
    df_e = df_e[column_names]
    mode = 'w' if header else 'a'
    df_e.to_csv('csvPiyu/1.2_info_classified.csv', encoding='utf-8', mode=mode, header=True, index=False)

print("comments classified...")

# calling for regression models to get values for comments
regression_model.regression_model_for_testing_func()

# extracting year from the posted time
extract_year.extract_year_func()

# giving weight by year and getting mean scores
final_score.final_score_calculation_func()
