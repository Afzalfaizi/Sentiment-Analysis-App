import streamlit as st # pip install streamlit
from textblob import TextBlob  # pip install textblob
import nltk     #pip install nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

st.title("Sentiment Analysis App") 

user_input = st.text_input("Enter some text:", "Sample input")

# Additional sentiment categories
positive_emotions = ['Happy', 'Joyful', 'Excited', 'Delighted']  
negative_emotions = ['Sad', 'Depressed', 'Upset', 'Miserable']
wonder_emotions = ['Wonder', 'Curious', 'Interested', 'Fascinated']

def analyze_sentiment(text):
  blob = TextBlob(text)
  analyzer = SentimentIntensityAnalyzer()
  return analyzer.polarity_scores(text)

if user_input:

  sentiment = analyze_sentiment(user_input)
  
  compound = sentiment['compound']

  if compound > 0.5:
    sentiment_category = random.choice(positive_emotions)
  elif compound < -0.5:
    sentiment_category = random.choice(negative_emotions)
  elif 'wonder' in user_input or 'curious' in user_input:
    sentiment_category = random.choice(wonder_emotions)
  elif compound > 0:
    sentiment_category = 'Positive'
  elif compound < 0:
    sentiment_category = 'Negative'
  else:
    sentiment_category = 'Neutral'

  sentiment_emojis = {
    'Positive': '🙂',
    'Negative': '🙁',
    'Neutral': '😐',
    'Happy': '😊',
    'Joyful': '😄',
    'Excited': '🤩',
    'Delighted': '😀',
    'Sad': '😔',
    'Depressed': '😭',
    'Upset': '😖',
    'Miserable': '😣',
    'Wonder': '🤔',
    'Curious': '🧐', 
    'Interested': '😮',
    'Fascinated': '✨'
  }

  st.markdown(f"## Sentiment Category: {sentiment_category} {sentiment_emojis[sentiment_category]}")
  st.write("### Sentiment Scores:", sentiment)
  
# Add Author Details
st.markdown("---")
st.markdown("### Author: Muhammad Afzal")
# add yourutube icon with hyper link
st.markdown("Data Scientist")

st.markdown("### Connect with us and learn more from here")


st.markdown("""<div style="display: flex; align-items:center;">
  
  <a href="https://www.linkedin.com/in/mafzalfaizi/" target="_blank">
    <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/linkedin.svg" width="50" style="margin-right: 10px;">
  </a>

  <a href="https://github.com/Afzalfaizi" target="_blank">
    <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="50" style="margin-right: 10px;">
  </a>

  <a href="https://www.facebook.com/Afzalfaizii/" target="_blank">
    <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/facebook.svg" width="50">
  </a>
</div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("For any query")
st.markdown("contact: afzaalm993@gmail.com")