## Importing Lib's
import numpy as np
import tensorflow as tf
import streamlit as st
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model

## Loading IMDB dataset Word Index
windex=imdb.get_word_index()
rindex={value: key for key, value in windex.items()}

## Loading Model
model = load_model('simple_rnn_imdb.h5')

## Helper Functions
# Function To Decode Reviews
def decode_review(encode_review):
    return ' '.join([rindex.get(i - 3,"?")for i in encode_review])

# Function To Preprocess User Input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [windex.get(word, 2) + 3 for word in words]
    padding_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padding_review

## Prediction Function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)

    prediction = model.predict(preprocessed_input)

    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    return sentiment, prediction[0][0]

## Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

## User Input

user_input = st.text_area('Movie Review')

if st.button('Classify'):
    sentiment,score = predict_sentiment(user_input)
    st.write(f'Sentiment : {sentiment}')
    st.write(f'Prediction Score : {score}')
else:
    st.write('Please enter a movie review.')