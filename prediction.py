import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the pre-trained Random Forest model from the .pkl file
with open('optimized_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def show_predict_page():
    st.title("🎮 Player Playtime and Retention Prediction for Video Games 🎮")

    # Kategorik veri seçenekleri
    top_5_platforms = ['PC', 'PlayStation', 'Xbox', 'Apple Macintosh', 'Nintendo']
    top_8_genres = ['Action', 'Adventure', 'Indie', 'RPG', 'Shooter', 'Strategy', 'Simulation', 'Casual']

    # Kullanıcıdan input alma
    rating = st.slider("Rating", 0.0, 5.0, 4.0)
    metacritic = st.slider("Metacritic", 0, 100, 90)
    
    genre = st.selectbox("Genre", top_8_genres)
    platform = st.selectbox("Platform", top_5_platforms)

    # Input verilerini hazırlama
    input_data = {
        'rating': rating,
        'metacritic': metacritic,
        'genre_Action': 1 if genre == 'Action' else 0,
        'genre_Adventure': 1 if genre == 'Adventure' else 0,
        'genre_Indie': 1 if genre == 'Indie' else 0,
        'genre_RPG': 1 if genre == 'RPG' else 0,
        'genre_Shooter': 1 if genre == 'Shooter' else 0,
        'genre_Strategy': 1 if genre == 'Strategy' else 0,
        'genre_Simulation': 1 if genre == 'Simulation' else 0,
        'genre_Casual': 1 if genre == 'Casual' else 0,
        'platform_PC': 1 if platform == 'PC' else 0,
        'platform_PlayStation': 1 if platform == 'PlayStation' else 0,
        'platform_Xbox': 1 if platform == 'Xbox' else 0,
        'platform_Apple Macintosh': 1 if platform == 'Apple Macintosh' else 0,
        'platform_Nintendo': 1 if platform == 'Nintendo' else 0
    }

    # Veriyi dataframe formatına çevirme
    columns = [
        'rating', 'metacritic',
        'genre_Action', 'genre_Adventure', 'genre_Indie', 'genre_RPG',
        'genre_Shooter', 'genre_Strategy', 'genre_Simulation', 'genre_Casual',
        'platform_PC', 'platform_PlayStation', 'platform_Xbox',
        'platform_Apple Macintosh', 'platform_Nintendo'
    ]
    
    X_user = pd.DataFrame([input_data], columns=columns)

    # Prediction butonunu ekleyelim
    if st.button("Prediction"):
        # Tahmin yapma
        predicted_playtime = model.predict(X_user)

        # Tahmin sonucunu renkli olarak gösterme
        color = "red" if predicted_playtime[0] < 15 else "green"
        return_message = "The player is likely to return!" if predicted_playtime[0] >= 15 else "The player is not likely to return!"

        # Tahmin ve mesajı gösterme
        st.markdown(f"""
            <p style="text-align: left; font-weight: bold; color: {color};">
                Predicted Playtime: {predicted_playtime[0]:.2f} hours --> {return_message}
            </p>
        """, unsafe_allow_html=True)
