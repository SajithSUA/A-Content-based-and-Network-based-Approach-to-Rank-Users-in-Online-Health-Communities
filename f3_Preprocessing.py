# nltk.download('stopwords')
from sklearn.datasets import load_files
from nltk.corpus import stopwords
from termcolor import colored
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from gensim.models import Word2Vec
import gensim
from sklearn.decomposition import PCA
from gensim.models import KeyedVectors
from sklearn.feature_selection import SelectKBest
from textblob import TextBlob
from gensim.scripts.glove2word2vec import glove2word2vec
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re


def main(df):
    # remove most frequent words
    most_freq = pd.Series(' '.join(df['comment']).split()).value_counts()[:50]
    # print(most_freq)
    most_freq = list(most_freq.index)
    df['comment'] = df['comment'].apply(lambda x: " ".join(x for x in x.split() if x not in most_freq))
    #print(df['comment'])

    # remove rare words
    least_freq = pd.Series(' '.join(df['comment']).split()).value_counts()[-10:]
    # print(least_freq)
    freq = list(least_freq.index)
    df['comment'] = df['comment'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    #print(df['comment'])

    # commented because this takes a lot of time
    # spelling corrections ex: ur = your
    # df['comment'] = df['comment'].apply(lambda x: str(TextBlob(x).correct()))

    # df['comment'] = str(df['comment'])


    documents = []
    tokened_doc = []
    for i in range(0, len(df)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', df['comment'][i])
        # document = str(document)
        # print(document)
        # print("\n")

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # print(document)
        # print("\n")

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        # print(document)
        # print("\n")

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # print(document)
        # print("\n")

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        # print(document)
        # print("\n")

        # Removing numbers
        document = re.sub(r'\d+', '', document)
        # print(document)
        # print("\n")

        # remove white space characters DON'T USE
        # document = ''.join(document.split())
        # print(document)
        # print("\n")

        # Converting to Lowercase
        document = document.lower()
        # print(document)
        # print("\n")

        # tokenization & stop words removal
        # document = nltk.word_tokenize(document)
        # # print(tokens)
        # document = " ".join([word for word in document if word not in stopwords.words('english')])
        # print(document)
        # print("\n")

        # for word2vec
        tok_sen = nltk.word_tokenize(document)

        # tokenization & lemmatization /CHECK WITH STEMMER
        lemmatizer = WordNetLemmatizer()
        tokens = nltk.word_tokenize(document)
        document = ' '.join([lemmatizer.lemmatize(w) for w in tokens])
        # print(document)
        # print("\n")

        # pos tagging
        word_tokens = word_tokenize(document)
        pos_tagged = nltk.pos_tag(word_tokens)
        # print(pos_tagged)

        documents.append(document)
        # tokened_doc.append(tok_sen)

    print("comments preprocessed...")
    return documents

if __name__=='__main__':
    main()