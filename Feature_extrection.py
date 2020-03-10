import pickle
import nltk
import string
import re
import gensim
import heapq
import collections
import datetime
import csv
import pandas as pd
import Normalized_feature
import Linnear_Regression

from nltk.corpus import stopwords

stopwords_english = stopwords.words('english')

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

from nltk.tokenize import TweetTokenizer

from nltk.corpus import wordnet

# Happy Emoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])

# all emoticons (happy + sad)
emoticons = emoticons_happy.union(emoticons_sad)


def clean_comments(comment):
    # remove stock market tickers like $GE
    comment = re.sub(r'\$\w*', '', comment)
    # remove hyperlinks
    comment = re.sub(r'https?:\/\/.*[\r\n]*', '', comment)
    # remove hashtags
    # only removing the hash # sign from the word
    comment = re.sub(r'#', '', comment)
    comment = re.sub(r' rt ', '', comment)
    comment = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", comment).split())
    # only removing the hash : sign from the word
    comment = re.sub(r':', '', comment)
    # remove numbers
    comment = re.sub(r'\d+', '', comment)
    # remove punctuation
    comment = comment.translate(str.maketrans('', '', string.punctuation))
    # remove emojis
    comment = comment.encode('ascii', 'ignore').decode('ascii')

    return comment


def tokenize_comments(clean_comment):
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(clean_comment)
    return tweet_tokens

def lemmatize_tokens(comment_tokens):
    comments_clean = []
    for word in comment_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in emoticons and  # remove emoticons
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            # stem_word = stemmer.stem(word) # stemming word
            stem_word = lemmatizer.lemmatize(word)  # lemmatize word
            comments_clean.append(stem_word)
    return comments_clean

def lda_model(words_list):
    from gensim import corpora, models
    dictionary = corpora.Dictionary(words_list)
    words_dictionary = [dictionary.doc2bow(words) for words in words_list]

    ldamodel = gensim.models.ldamodel.LdaModel(words_dictionary, num_topics=5, id2word=dictionary, passes=10)
    print(ldamodel.print_topics())
    return ldamodel

def word_comparisn(tokens, synonyms):
    # print(set(synonyms))
    updateness_feature1 = 1
    for token in tokens:
        for synonym in synonyms:
            if token == synonym:
                updateness_feature1 = updateness_feature1 + 1
    return updateness_feature1

def bag_of_words(words_list):
    from collections import Counter
    from operator import itemgetter
    a = open(r"WordCount.csv", "w+", encoding="utf-8")
    freqs = {}
    for words in words_list:
        for word in words:
            if word not in freqs:
                freqs[word] = 1
            else:
                freqs[word] += 1
    sortedWords = sorted(freqs.items(), key=itemgetter(1), reverse=True)

    for sortedWord in sortedWords:
        print(sortedWord)

def Transform_date_feature(date):
    res = date[: -2]
    # d1 = datetime.strptime(d1, "%Y-%m-%d")
    today = "JAN 01 2020 00:00"
    date = datetime.datetime.strptime(res, "%b %d %Y  %H:%M")
    date2 = datetime.datetime.strptime(today, "%b %d %Y  %H:%M")
    date_feature = abs((date2 - date).days)
    # print (date_feature)
    return date_feature

def All_LDA_Terms():
    synonyms = ["mammo","mammogram","radiologist","mammography","anxiety","mm","mri"]
    for syn in wordnet.synsets("biopsy"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    for syn in wordnet.synsets("Ultrasound"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    for syn in wordnet.synsets("benign"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms

def All_Trending_Terms():
    Trending_Terms = ["sabcs","tamoxifen","pas","cyst","lymph","hypoechoic","lesion","lump","birads","fibroadenoma","mass"
                      "bcrf","metastasis","bcsm","amp","ampk"]
    for syn in wordnet.synsets("underbelly"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("thrivers"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("fundraising"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("fragrance"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("chemical"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("toxicity"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    for syn in wordnet.synsets("Malignant"):
        for l in syn.lemmas():
            Trending_Terms.append(l.name())
    return Trending_Terms

def Uptodatedness_score():
    with open(r"E:\FYP\Data_Source\merged_csvs_data.csv","r",encoding="utf8") as readCSV:
        cu = open(r"CSV_files\comment_updateness_original.csv","w+",encoding="utf-8")
        #test = open(r"test.txt", "w+", encoding="utf-8")
        cu.write("comment_id,name,Date_feature,trending_feature,LDA_feature,Updateness\n")
        CSVfile = csv.reader(readCSV, delimiter=',')
        words_list = []
        count=1
        for row in CSVfile:
            clean_comment = clean_comments(row[5])
            tokenize_comment = tokenize_comments(clean_comment)
            tokens = lemmatize_tokens(tokenize_comment)
            words_list.append(tokens)
            date_feature = Transform_date_feature(str(row[1]))
            updateness_feature1=word_comparisn(tokens,All_LDA_Terms())
            updateness_feature2=word_comparisn(tokens,All_Trending_Terms())
            cu.write(str(count)+","+str(row[4])+","+str(date_feature)+","+str(updateness_feature2)+","+str(updateness_feature1)+",\n")
            count=count+1
            #print(count,row[4],date_feature,updateness_feature2,updateness_feature1)

    Normalized_feature.Normalized_features()
    Linnear_Regression.Predict_Score()