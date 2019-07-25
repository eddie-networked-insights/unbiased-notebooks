#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from keras.models import Model
from keras.layers import Input, Dense, Embedding, SpatialDropout1D, Dropout, add, concatenate
from keras.layers import CuDNNLSTM, Bidirectional, GlobalMaxPooling1D, GlobalAveragePooling1D
from keras.optimizers import Adam
from keras.preprocessing import text, sequence

from keras.models import load_model


# In[3]:


model = load_model("second-model-2019-06-26 14:19:54.312555.h5")


# In[ ]:


import pickle

with open('tokenizer.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    tokenizer = pickle.load(f)


# In[ ]:


NUM_MODELS = 2
# the maximum number of different words to keep in the original texts
# 40_000 is a normal number
# 100_000 seems good too
MAX_FEATURES = 100000 

#this is the number of training sample to put in theo model each step
BATCH_SIZE = 512

#units parameters in Keras.layers.LSTM/cuDNNLSTM
#it it the dimension of the output vector of each LSTM cell.
LSTM_UNITS = 128
DENSE_HIDDEN_UNITS = 4 * LSTM_UNITS

EPOCHS = 4

#we will convert each word in a comment_text to a number.
#So a comment_text is a list of number. How many numbers in this list?
#we want the length of this list is a constant -> MAX_LEN
MAX_LEN = 220


# In[ ]:


strHist = {}


# In[ ]:


#one liner to get prediction for any string using the last model (NOTE: removes words that aren't in tokenizer.word_index)
inputStr = "Networked Insights is the best"
strHist[inputStr] = model.predict(sequence.pad_sequences(tokenizer.texts_to_sequences(np.array([inputStr], dtype=object)), maxlen=MAX_LEN), batch_size=2048)[0].flatten()[0]


# In[ ]:


strHist


# In[ ]:


while True:
    inputStr = input("(Ctrl+G ENTER to quit) input> ")
    if inputStr == '\x07':
        break
    outputVar = model.predict(sequence.pad_sequences(tokenizer.texts_to_sequences(np.array([inputStr], dtype=object)), maxlen=MAX_LEN), batch_size=2048)[0].flatten()[0]
    print(outputVar)

