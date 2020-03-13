from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import pickle
from scipy.sparse import hstack
import f3_Preprocessing as pre


def regression_model_for_testing_func():

    df_of_emo_csv = pd.read_csv('csvPiyu/1.1_emo_classified.csv', encoding="utf-8")
    name_in_emo_csv = df_of_emo_csv['name']
    posted_time_in_emo_csv = df_of_emo_csv['posted_time']
    documents_emo = pre.main(df_of_emo_csv)  # passed for preprocessing

    df_of_info_csv = pd.read_csv('csvPiyu/1.2_info_classified.csv', encoding="utf-8")
    name_in_info_csv = df_of_info_csv['name']
    posted_time_in_info_csv = df_of_info_csv['posted_time']
    documents_info = pre.main(df_of_info_csv)    # passed for preprocessing


    # create corpus of emotional comments
    corpus_emo = []
    emo_document_length = []
    for i in documents_emo:
        corpus_emo.append(i)
        emo_document_length.append(len(i.split()))

    # print("emo_corpus", corpus_emo)
    # print("emo_length", emo_document_length)

    vectorizer = CountVectorizer(max_features=1500, ngram_range=(3, 3), stop_words=stopwords.words('english'))
    X_emo = vectorizer.fit_transform(corpus_emo).toarray()

    tfidfconverter = TfidfTransformer()
    X_emo = tfidfconverter.fit_transform(X_emo).toarray()

    # X_emo = hstack([X_emo, emo_document_length])

    load_model_emo = pickle.load(open("predict_model_for_emo_level.sav", 'rb'))

    result_emo = load_model_emo.predict(X_emo)
    # print(result_emo[0])



    # create corpus of informational comments
    corpus_info = []
    info_document_length = []
    for i in documents_info:
        corpus_info.append(i)
        info_document_length.append(len(i.split()))

    vectorizer = CountVectorizer(max_features=1500, ngram_range=(3, 3), stop_words=stopwords.words('english'))
    X_info = vectorizer.fit_transform(corpus_info).toarray()

    tfidfconverter = TfidfTransformer()
    X_info = tfidfconverter.fit_transform(X_info).toarray()

    # X_info = hstack([X_info, info_document_length])

    load_model_info = pickle.load(open("predict_model_for_info_level.sav", 'rb'))

    result_info = load_model_info.predict(X_info)


    # concatenating 2 csv's together
    names_by_comments = [*name_in_info_csv, *name_in_emo_csv] #216
    dates_by_comments = [*posted_time_in_info_csv, *posted_time_in_emo_csv]
    info_levels_by_comments = []
    emo_levels_by_comments = []

    # ????????????????
    index = 1
    for i in names_by_comments:
        if index <= len(name_in_info_csv):
            info_levels_by_comments.append(result_info[index-1])
            emo_levels_by_comments.append(0)
        elif index > len(name_in_info_csv):
            info_levels_by_comments.append(0)
            emo_levels_by_comments.append(result_emo[((index - len(name_in_info_csv)) - 1)])
        index = index + 1


    dataFrame = pd.DataFrame()

    dataFrame['name'] = names_by_comments
    dataFrame['posted_time'] = dates_by_comments
    dataFrame['Info_score'] = info_levels_by_comments
    dataFrame['Emo_score'] = emo_levels_by_comments

    dataFrame.to_csv(r'csvPiyu/2_support_scores_predicted_for_comments.csv', encoding="utf-8")

    print("support scores for comments predicted...")


