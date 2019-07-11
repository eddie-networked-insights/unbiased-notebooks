from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

print(40*'-')
print("START OF INITIALIZATION")
print(40*'-')

# In[1]:
import tensorflow as tf


import numpy as np
import pandas as pd
from tqdm import tqdm
tqdm.pandas()
from keras.models import Model
from keras.layers import Input, Dense, Embedding, SpatialDropout1D, Dropout, add, concatenate
from keras.layers import CuDNNLSTM, Bidirectional, GlobalMaxPooling1D, GlobalAveragePooling1D
from keras.optimizers import Adam
from keras.preprocessing import text, sequence
from keras.callbacks import LearningRateScheduler

from keras.models import load_model


# In[2]:

global model
model = load_model("second-model-2019-06-26 14:19:54.312555.h5")
global graph
graph = tf.get_default_graph()

# In[4]:


import pickle

with open('tokenizer.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    tokenizer = pickle.load(f)


# In[8]:


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



#print("type(predict) ",type(predict))
#print("PREDICT",predict)
#print("RESULT",result)




print(40*'-')
print("END OF INITIALIZATION")
print(40*'-')

@app.route("/")
def hello():
    content = request.args.get('content')
    #print(result)



    
    # In[10]:
    #one liner to get prediction for any string using the last model (NOTE: removes words that aren't in tokenizer.word_index)
    inputStr = content#"Trump is a piece of shit"
    print("DEBUG")
    foo1 = np.array([inputStr], dtype=object)
    print("DEBUG")
    foo2 = tokenizer.texts_to_sequences(foo1)
    print("DEBUG")
    foo3 = sequence.pad_sequences(foo2, maxlen=MAX_LEN)
    print("DEBUG")


#    print(type(model))
#    tf.keras.backend.clear_session()
#    print(type(model))

    with graph.as_default():
        foo4 = model.predict(foo3, batch_size=BATCH_SIZE)
    print("DEBUG")
    foo5 = foo4[0]
    print("DEBUG")
    foo6 = foo5.flatten()
    print("DEBUG")
    predict = foo6[0]
    print("DEBUG")
    #result = {"content":inputStr,"prediction":int(predict*100)}
    result = {"content":inputStr,"prediction":float(predict)}#.99
    print("DEBUG")




    return jsonify(result)
    #return "Hello World!"
