import streamlit as st
import pickle
import pandas as pd
import random


import pickle

# Daha önce kaydedilen model ve sütun bilgilerini yükleme
with open('playtime_model.pkl', 'rb') as model_file:
    data = pickle.load(model_file)
    model = data['model']  # Modeli yükle
    expected_columns = data['columns']  # Modelin eğitim sırasında gördüğü sütunlar




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
        f'genre_{genre}': 1,
        f'platform_{platform}': 1
    }

    # Diğer sütunları sıfıra ayarlama
    for column in expected_columns:
        if column not in input_data:
            input_data[column] = 0

    # Veriyi DataFrame formatına çevirme
    X_user = pd.DataFrame([input_data], columns=expected_columns)

    # Prediction butonunu ekleyelim
    if st.button("Prediction"):
        # Predict
        predicted_playtime = model.predict(X_user)

        # Tahmin sonucunu renkli olarak gösterme
        color = "red" if predicted_playtime[0] < 5 else "green"
        return_message = "The player is likely to return!" if predicted_playtime[0] >= 5 else "The player is not likely to return!"

        # Predict and See the message
        st.markdown(f"""
            <p style="text-align: left; font-weight: bold; color: {color};">
                Predicted Playtime: {predicted_playtime[0]/10:.2f} hours --> {return_message}
            </p>
        """, unsafe_allow_html=True)

        rounded_playtime = round((predicted_playtime[0])/10)
        
        # Read CSV
        df = pd.read_csv("final_game_data.csv")

        # Search the rounded values in 'playtime' column
        matched_rows = df[df['playtime'] == rounded_playtime]

         # Print the result
        if not matched_rows.empty:
            st.markdown(f"""
                <p style="text-align: left; font-weight: bold;">
                    Game(s) the player may have played <br>
                </p>
            """, unsafe_allow_html=True)

            if len(matched_rows) > 5:
               sampled_rows = matched_rows.sample(n=5, random_state=42)
            else:
               sampled_rows = matched_rows

            for _, row in sampled_rows.iterrows():
                game_name = row['name']
                st.markdown(f"""
                    <p style="text-align: left; font-weight: bold;">
                        Game: {game_name}
                    </p>
                """, unsafe_allow_html=True)

                # Process screenshots for the current game
                screenshots = eval(row['short_screenshots'])  # Convert string to list if necessary
                random_screenshots = random.sample(screenshots, min(3, len(screenshots)))

                for screenshot in random_screenshots:
                    st.image(screenshot['image'], use_container_width=True)

        else:
            st.markdown(f"""
                <p style="text-align: left; font-weight: bold;">
                    Game(s) the player may have played --> No matching games found in the dataset.
                </p>
            """, unsafe_allow_html=True)

