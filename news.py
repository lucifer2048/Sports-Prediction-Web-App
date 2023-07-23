import requests
import streamlit as st
import numpy as np
import json

#to get yesterday's date
from datetime import date
from datetime import timedelta
today = date.today()
yesterday = today - timedelta(days=1)
def fetch_news():
    st.title('Latest headlines')

    query1 =["Tennis", "Cricket", "Football", "Basketball", "F1"]

    query = st.selectbox("Choose among the top sports news", ["Tennis", "Cricket", "Football", "Basketball", "F1"])
    url = f"https://newsapi.org/v2/everything?q={query}&from={yesterday}&sortBy=publishedAt&language=en&apiKey=97b70534bdc54e10b54383c146b4990c"
    r = requests.get(url)
    news = json.loads(r.text)


    
    for article in news["articles"]:
        st.container()
        st.write('###', article["title"])
        st.write(article["description"])

