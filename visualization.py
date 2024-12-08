import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("final_game_data.csv")

# Ensure the 'released' column is converted to datetime and extract the year
if 'released' in df.columns:
    df['released'] = pd.to_datetime(df['released'], errors='coerce')  # Convert to datetime
    df['year'] = df['released'].dt.year  # Extract the year
else:
    st.error("The 'released' column is missing from the dataset!")

def show_explore_page():
  
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

    
    # **4. Pairplot for Rating and Reviews Count**
    # Filter the dataset for playtime less than 180
    df2 = df[df['playtime'] < 20]
    st.write("### Pairplot for Rating and Reviews Count (Filtered for Playtime < 20)")
    pairplot = sns.pairplot(df2, vars=['rating', 'reviews_count'], hue='playtime', palette="viridis", height=4)
    pairplot.fig.suptitle("Pairplot for Rating and Reviews Count (Target: Playtime)", y=1.02)
    st.pyplot(pairplot.fig)

     
   # **Distribution of Playtime by Year**
    st.write("### Distribution of Playtime by Year")
    if 'year' in df.columns:
        avg_playtime_by_year = df.groupby('year')['playtime'].mean()

        # Normalize playtime for colormap
        norm = plt.Normalize(avg_playtime_by_year.min(), avg_playtime_by_year.max())
        colors = plt.cm.magma(norm(avg_playtime_by_year.values))

        # Plot the distribution with a colormap
        fig, ax = plt.subplots(figsize=(10, 6))
        for i in range(len(avg_playtime_by_year) - 1):
            ax.plot(
                avg_playtime_by_year.index[i:i+2], 
                avg_playtime_by_year.values[i:i+2], 
                color=colors[i], 
                linewidth=2.5
            )
        
        # Add the colorbar
        sm = plt.cm.ScalarMappable(cmap="magma", norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, ax=ax)
        cbar.set_label("Average Playtime (hours)")

        # Add titles and labels
        ax.set_title("Average Playtime by Year", fontsize=16)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Average Playtime (hours)", fontsize=12)
        ax.grid(True)

        # Render the plot in Streamlit
        st.pyplot(fig)
    else:
        st.error("The 'year' column is missing! Check if the 'released' column is correctly formatted.")


    