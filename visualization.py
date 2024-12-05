import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("final_game_data.csv")

def show_explore_page():
    st.title("Explore Salaries and Playtime Data")

    # **1. Playtime Distribution KDE Plot**
    st.write("### Distribution of Playtime")
    plt.figure(figsize=(8, 4))
    sns.kdeplot(df['playtime'], fill=True, color='blue', alpha=0.6)
    plt.title('Distribution of Playtime', fontsize=16)
    plt.xlabel('Playtime (hours)', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.grid(True)
    st.pyplot(plt)

    # **2. Average Playtime by ESRB Rating**
    st.write("### Average Playtime by ESRB Rating")
    avg_playtime_by_esrb = df.groupby(['esrb_rating'])['playtime'].mean().sort_values(ascending=True)

    # ESRB Rating labels for better readability
    esrb_rating_labels = [
        'Adults Only', 'Teen', 'Everyone 10+', 'Everyone', 'Mature', 'Rating Pending', 'SinglePlayer'
    ]
    
    # Bar Chart with 'coolwarm' palette for ESRB ratings
    plt.figure(figsize=(8, 6))
    avg_playtime_by_esrb.plot(kind='bar', color=sns.color_palette("coolwarm", len(avg_playtime_by_esrb)))
    
    # Update the x-axis labels to use the readable ESRB ratings
    plt.xticks(ticks=range(len(esrb_rating_labels)), labels=esrb_rating_labels, rotation=45)

    plt.title('Average Playtime by ESRB Rating', fontsize=16)
    plt.xlabel('ESRB Rating', fontsize=12)
    plt.ylabel('Average Playtime (hours)', fontsize=12)
    st.pyplot(plt)

    # **3. Ratings and Metacritic vs. Playtime (Bubble Chart)**
    st.write("### Ratings and Metacritic vs. Playtime (Bubble Chart)")
    plt.figure(figsize=(10, 6))

    # Bubble chart: X = Metacritic, Y = Playtime, Size = Rating
    scatter = plt.scatter(
        x=df['metacritic'],        # X axis: Metacritic
        y=df['playtime'],          # Y axis: Playtime
        s=df['rating']*50,         # Bubble size: Rating (scaled)
        alpha=0.6,                 # Transparency
        c=df['rating'],            # Color by Rating
        cmap='viridis',            # Color map
        edgecolors="w",            # Border color
        linewidth=0.5              # Border width
    )

    # Add colorbar
    plt.colorbar(scatter, label='Rating')

    # Set title and labels
    plt.title('Ratings and Metacritic vs. Playtime (Bubble Chart)', fontsize=16)
    plt.xlabel('Metacritic Score', fontsize=12)
    plt.ylabel('Playtime (hours)', fontsize=12)

    # Show grid
    plt.grid(True)

    # Display the plot with hover functionality
    st.pyplot(plt)

    # Hover information display with Plotly (optional to implement)
    # st.write("Hover over the plot to see details (e.g., Ratings, Metacritic, Playtime)")
