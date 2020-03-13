import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Model
from tensorflow.keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

import pickle
#%matplotlib inline

df = pd.read_csv('1.support_type_labeled_for_classification.csv', delimiter=',', encoding='utf-8')
# df.head()

df.drop(['id', 'joined_date', 'no_of_posts'], axis=1, inplace=True)
# df.info()

# sns.countplot(df.type)
# plt.xlabel('Label')
# plt.title('Type Balancing')

X = df.comment
Y = df.type
le = LabelEncoder()  # normalize target labels
Y = le.fit_transform(Y)  # fit label encoder and return encoded labels
Y = Y.reshape(-1, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15)

max_words = 1000
max_len = 500
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train)
sequences = tok.texts_to_sequences(X_train)
sequences_matrix = sequence.pad_sequences(sequences, maxlen=max_len)


def RNN():
    inputs = Input(name='inputs', shape=[max_len])
    layer = Embedding(max_words, 50, input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256, name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(1, name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs, outputs=layer)
    return model


model = RNN()
print(model.summary())
model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# print
model.fit(sequences_matrix, Y_train, batch_size=128, epochs=40,
          validation_split=100, callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])


test_sequences = tok.texts_to_sequences(X_test)
test_sequences_matrix = sequence.pad_sequences(test_sequences, maxlen=max_len)
accuracy = model.evaluate(test_sequences_matrix, Y_test)
# print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accuracy[0], accuracy[1]))

####
# sample_texts_pos = ["WC3 They missed my cancer on both the mammogram and ultrasound but I had extremely dense breasts. If you have fatty breasts then the mammogram is less likely to miss IDC but may still miss ILC. Maybe someone more familiar with that can chime in but if an MRI would give you peace of mind then I don't think it unreasonable for you to request one. Personally I think baseline breast MRIs should be standard."]
# sample_texts_neg = ["So glad to hear that Epic...I have been down that road before and it really does help. I think it takes a lot of courage to make that first appointment and go but it helps so much. :-)"]
#
# txts = tok.texts_to_sequences(sample_texts_pos)
# txts = sequence.pad_sequences(txts, maxlen=max_len)
# preds = model.predict(txts)
# print(preds)
#
# txts = tok.texts_to_sequences(sample_texts_neg)
# txts = sequence.pad_sequences(txts, maxlen=max_len)
# preds = model.predict(txts)
# print(preds)


# save model and architecture to single file
model.save("RNN_Model.h5")
# saving
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tok, handle, protocol=pickle.HIGHEST_PROTOCOL)

