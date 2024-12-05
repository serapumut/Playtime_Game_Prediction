import streamlit as st
from prediction import show_predict_page
from visualization import show_explore_page

# Title in the sidebar with adjusted font size
st.sidebar.markdown("""
    <h2 style="font-size: 18px;">Application for predicting playtime and whether returning to a video game or not.</h2>
""", unsafe_allow_html=True)


# Sayfa geçişi için seçici
page = st.sidebar.selectbox("Predict or Visualization", ("Predict", "Visualization"))

# Explanation text under the selectbox
st.sidebar.markdown("""
    This app predicts how much a player will spend on playtime and whether they are likely or unlikely to return to a video game based on game-related features.
    
    In order to do this, this app uses machine learning. It loads a pre-trained Random Forest model, which takes as input various features of the game, such as the game's rating, its Metacritic score, the genre of the game, and the platform on which it is played (e.g., PlayStation, PC, Xbox).
                    
    The app preprocesses the input data by encoding categorical features (such as genre and platform) and combining others, creating a well-structured input for the model. Based on these features, the app predicts the expected playtime of the user and estimates the probability of the player returning to the game.
""")

if page == "Predict":
    show_predict_page()  # Prediction sayfasını aç
else:
    show_explore_page()  # Visualization sayfasını aç
