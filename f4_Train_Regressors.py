from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from termcolor import colored
from gensim.models import Word2Vec
import gensim
from sklearn.decomposition import PCA
from gensim.models import KeyedVectors
from sklearn.feature_selection import SelectKBest
from gensim.scripts.glove2word2vec import glove2word2vec
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import FunctionTransformer
from scipy.sparse import hstack
from scipy import sparse
import pickle
from sklearn.ensemble import RandomForestRegressor
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import f3_Preprocessing as pre


df = pd.read_csv(
    'C:/Users/Piyumi/PycharmProjects/uptoSplit/training_datasets/2.1.emo_level_labeled_for_training.csv', encoding="utf-8")
# df = pd.read_csv(
#     'C:/Users/Piyumi/PycharmProjects/uptoSplit/training_datasets/2.2.info_level_labeled_for_training.csv', encoding="utf-8")

# calling preprocessing function
documents = pre.main(df)

# create corpus of comments
corpus = []
document_length = []
for i in documents:
    corpus.append(i)
    document_length.append(len(i.split()))


# X = df['comment']
y = df['level']


vectorizer = CountVectorizer(max_features=1500, ngram_range=(3, 3), stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

# X = hstack([X, document_length])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=1500, random_state=0)

model.fit(X_train, y_train)

y_predict = model.predict(X_test)

fileName = "predict_model_for_emo_level.sav"  # done separately
# fileName = "predict_model_for_info_level.sav"
pickle.dump(model, open(fileName, 'wb'))


df = pd.DataFrame({'Actual': y_test, 'predicted': y_predict})
compared_df = df.head(25)
# print(compared_df)

# print('means absolute error', metrics.mean_absolute_error(y_test, y_predict))

# checking accuracy
errors = abs(y_predict - y_test)
print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)

# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
