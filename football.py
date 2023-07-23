import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder


def load_model():
    with open('football_saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model()

best = data["model"]
home = data["home"]
Away = data["Away"]


def show_details():
    st.title("Premier League winner prediction")
    st.write("Lets predict next ")
    
    Team1 = ('Coventry City', 'Leeds United', 'Sheffield Utd', 'Crystal Palace',
       'Arsenal', 'Ipswich Town', 'Everton', 'Southampton', 'Chelsea',
       "Nott'ham Forest", 'Manchester City', 'Blackburn', 'Wimbledon',
       'Tottenham', 'Liverpool', 'Aston Villa', 'Oldham Athletic',
       'Middlesbrough', 'Norwich City', 'QPR', 'Manchester Utd',
       'Sheffield Weds', 'Newcastle Utd', 'West Ham', 'Swindon Town',
       'Leicester City', 'Bolton', 'Sunderland', 'Derby County',
       'Barnsley', 'Charlton Ath', 'Watford', 'Bradford City', 'Fulham',
       'Birmingham City', 'West Brom', 'Portsmouth', 'Wolves',
       'Wigan Athletic', 'Reading', 'Hull City', 'Stoke City', 'Burnley',
       'Blackpool', 'Swansea City', 'Cardiff City', 'Bournemouth',
       'Brighton', 'Huddersfield', 'Brentford'
    )
    Team2 = (
        'Middlesbrough', 'Wimbledon', 'Manchester Utd', 'Blackburn',
       'Norwich City', 'Aston Villa', 'Sheffield Weds', 'Tottenham',
       'Oldham Athletic', 'Liverpool', 'QPR', 'Arsenal', 'Ipswich Town',
       'Coventry City', 'Sheffield Utd', 'Leeds United', 'Crystal Palace',
       'Manchester City', 'Chelsea', 'Southampton', 'Everton',
       "Nott'ham Forest", 'Swindon Town', 'West Ham', 'Newcastle Utd',
       'Leicester City', 'Bolton', 'Derby County', 'Sunderland',
       'Barnsley', 'Charlton Ath', 'Bradford City', 'Watford', 'Fulham',
       'West Brom', 'Birmingham City', 'Wolves', 'Portsmouth',
       'Wigan Athletic', 'Reading', 'Stoke City', 'Hull City', 'Burnley',
       'Blackpool', 'Swansea City', 'Cardiff City', 'Bournemouth',
       'Huddersfield', 'Brighton', 'Brentford'
    )
    
    Winner_Team={2:'Home',0:"Away",1:"Draw",}

    team1 = st.selectbox("Pick your Home team",Team1 )
    team2 = st.selectbox("Pick your Away team",Team2)
    button = st.button("predict")
    if button:
        X = np.array([[team1,team2]])
        X[:, 0] = home.transform(X[:,0])
        X[:, 1] = Away.transform(X[:,1])
        X = X.astype(float)
        
        winner = best.predict(X)
        winneris = Winner_Team[winner[0]]

        if winner == 2:
            st.title(f" {team1} will win")
        elif winner == 0:
            st.title(f"{team2} will win")
        else:
            st.subheader(f"the match will be a {winneris}")
