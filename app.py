import streamlit as st
import pickle
import pandas as pd
import base64
from PIL import Image

# Load trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Setup session state for popup display
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "win_prob" not in st.session_state:
    st.session_state.win_prob = 0
if "loss_prob" not in st.session_state:
    st.session_state.loss_prob = 0

# Function to encode background image to base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("C:/Users/Sujal Patel/Desktop/IPL_ML/captain.jpeg")

# Custom CSS
page_bg_img = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

.stApp {{
    background-image: url("data:image/png;base64,{bg_image}");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    font-family: 'Poppins', sans-serif;
}}

.block-container {{
    background-color: rgba(0, 0, 0, 0.95);
    padding: 2.5rem;
    border-radius: 20px;
    margin-top: 50rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
}}

h1 {{
    color: #FFD700;
    text-align: center;
    font-size: 48px;
    margin-bottom: 1rem;
}}

.stSelectbox > div {{
    font-size: 18px;
}}

input[type=number], .stNumberInput, .stSelectbox {{
    border-radius: 10px;
    background-color: #1c1c1c;
    color: white;
}}

.stButton>button {{
    background-color: #28a745;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px 24px;
    font-size: 20px;
    transition: all 0.3s ease-in-out;
    display: block;
    margin: 0 auto;
}}

.stButton>button:hover {{
    background-color: #1e7e34;
    transform: scale(1.05);
}}

.result-box {{
    animation: fadeInScale 1s ease-in-out;
    background: rgba(255, 255, 255, 0.1);
    border: 2px solid #FFD700;
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: #fff;
    margin-top: 30px;
    margin-bottom: 20px;
    box-shadow: 0 6px 30px rgba(255, 215, 0, 0.4);
    backdrop-filter: blur(6px);
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}}

@keyframes fadeInScale {{
    0% {{ opacity: 0; transform: scale(0.9); }}
    100% {{ opacity: 1; transform: scale(1); }}
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# App Title
st.markdown("# IPL 2025 VICTORY PREDICTOR")

# Static logos for all teams
teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Punjab Kings', 'Rajasthan Royals', 'Mumbai Indians',
         'Delhi Capitals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Lucknow Super Giants', 'Gujarat Titans']

# Function to load and display team logos statically
def display_static_logos():
    team_logos = {
        'CSK': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Chennai Super Kings.png',
        'KKR': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Kolkata Knight Riders.png',
        
        'PBKS': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Punjab Kings.png',
        'RR': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Rajasthan Royals.png',
        'MI': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Mumbai Indians.png',
        'DC': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Delhi Capitals.png',
        'RCB': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Royal Challengers Benguluru.png',
        'SRH': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Sunrisers Hyderabad.png',
        'LSG': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Lucknow Super Giants.png',
        'GT': 'C:/Users/Sujal Patel/Desktop/IPL_ML/team_logos/Gujarat Titans.png',
    }

    # Display all logos horizontally
    cols = st.columns(len(team_logos))
    for i, team in enumerate(team_logos):
        try:
            img = Image.open(team_logos[team])
            cols[i].image(img, caption=team, width=80)
        except Exception as e:
            cols[i].error(f"Error loading logo for {team}")

# Display the static team logos above the prediction box
display_static_logos()

# Team Selection
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🏏 Select Batting Team', teams)
with col2:
    bowling_team = st.selectbox('🎯 Select Bowling Team', [t for t in teams if t != batting_team])

# Venue and target
cities = ['Mumbai', 'Delhi', 'Chennai', 'Abu Dhabi', 'Visakhapatnam', 'Hyderabad', 'Chandigarh',
          'Ahmedabad', 'Bangalore', 'Jaipur', 'Kolkata', 'Port Elizabeth', 'Cuttack', 'Navi Mumbai',
          'Centurion', 'Bengaluru', 'Pune', 'Johannesburg', 'Dubai', 'Cape Town', 'Lucknow', 'Durban',
          'Dharamsala', 'Indore', 'East London', 'Sharjah', 'Guwahati', 'Raipur', 'Ranchi', 'Nagpur',
          'Kimberley', 'Bloemfontein']

selected_city = st.selectbox('📍 Select Venue', cities)
target = st.number_input('🎯 Target Score', min_value=1, step=1)

# Match Situation Inputs
col1, col2, col3 = st.columns(3)
with col1:
    score = st.number_input('🏏 Current Score', min_value=0, step=1)
with col2:
    overs = st.number_input("⏱ Overs Completed", min_value=0.1, max_value=20.0, step=0.1, format="%.1f")
with col3:
    wickets = st.number_input("❌ Wickets Down", min_value=0, max_value=10, step=1)

# Prediction button centered
if st.button('📊 Predict Winning Probability'):
    try:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_remaining = 10 - wickets
        crr = score / overs
        rrr = runs_left / (balls_left / 6)

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_remaining': [wickets_remaining],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        st.session_state.loss_prob = round(result[0][0]*100)
        st.session_state.win_prob = round(result[0][1]*100)
        st.session_state.show_result = True

        st.experimental_rerun()

    except Exception as e:
        st.error("⚠️ Error occurred. Please check your inputs!")
