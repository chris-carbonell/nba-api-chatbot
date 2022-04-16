# Dependencies

# general
from itertools import groupby
import re

# data
import numpy as np

# ml
import tensorflow as tf
from tensorflow import keras

# Constants

PATH_MODEL = "nba_api_chatbot/models/ner"
PATH_VOCABULARY = "nba_api_chatbot/data/vocabulary.txt"

MAPPING = {0: '[PAD]', 1: 'O', 2: 'B-PLAYER', 3: 'I-PLAYER', 4: 'B-STAT', 5: 'I-STAT'}  # via make_tag_lookup_table()

# Get Model

ner_model = keras.models.load_model(PATH_MODEL, compile=False)

# get vocabulary
with open(PATH_VOCABULARY, "r") as f:
    vocabulary = f.read().splitlines()

# get lookup layer
lookup_layer = keras.layers.StringLookup(
    vocabulary=vocabulary
)

# process text input
def tokenize_and_convert_to_ids(text):
    tokens = text.split(" ")
    return lookup_layer(tf.strings.lower(tokens))

def get_prediction(text):
    '''
    predict NER tags based on raw text
    '''

    # text = "How many field goals does Michael Jordan have?"

    text_scrub = text.rstrip("?")

    sample_input = tokenize_and_convert_to_ids(text_scrub)

    sample_input = tf.reshape(sample_input, shape=[1, -1])

    output = ner_model.predict(sample_input)
    prediction = np.argmax(output, axis=-1)[0]
    prediction = [MAPPING[i] for i in prediction]

    return prediction

def extract_tagged_values(text, prediction):
    '''
    extract the named entities from the raw text
    '''
    
    tokens = text.split(" ")
    
    regex = r"(?<=-).*"  # get text after hyphen (e.g., "STAT" from "B-STAT")
    
    # get named entities
    res = []
    i = 0
    for tag, chunk in groupby(re.findall(regex, tag) for tag in prediction):

        if tag != []:
            entity = []
            for j in chunk:
                # print(i, j)
                entity.append(tokens[i])
                i += 1

            res.append((tag[0], " ".join(entity)))
            
        else:
            i += len(list(chunk))

    # convert to dictionary
    # assume only one of each
    # if not, just take the first one
    d_res = {}
    for tup in res:
        if tup[0] not in d_res:
            d_res[tup[0]] = tup[1]

    return d_res