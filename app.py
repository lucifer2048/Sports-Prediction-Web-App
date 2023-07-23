import streamlit as st
from predict_cricket import show_predict_page
from news import fetch_news
from football import show_details

st.sidebar.title("Hello there.....")
st.sidebar.write("How you feeling today?")
selection = st.sidebar.selectbox("Explore", ("News","Premier league winner prediction","IPL winner prediction"))
if selection == "News":
    fetch_news()
elif selection == "Premier league winner prediction":
    show_details()
else:
    show_predict_page()
    