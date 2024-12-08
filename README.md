Player Playtime and Accordingly Retention Prediction for Video Games

The project, titled “Player Playtime and Accordingly Retention Prediction for Video Games,” focuses on developing a machine learning model to predict playtime and whether a player will return to a video game after their first session.
This project falls under the deployed predictive model category, as it involves creating a trained machine learning model and deploying it with a user-friendly interface.
This project will include an interactive and user-friendly deployment using Streamlit, a platform that simplifies app development and enhances user engagement.

Project Objective
The primary goal of this project is to predict player playtime and retention, helping game developers and publishers understand player behavior and improve engagement strategies.
The problem being addressed is how to identify the factors influencing a player’s playtime and likelihood of returning to a game, allowing for better-targeted interventions like personalized incentives or game design adjustments.

Data Source:
The dataset will be collected using the RAWG Video Games Database API, which provides detailed game-related information, including player ratings, release dates, genres, and platforms.
An API key has already been obtained for data access.

Data Collection Strategy:
Use the /games endpoint to retrieve data on popular and recently released games.
Implement request parameters for filtering (e.g., ordering by popularity and rating).
Handle missing or incomplete data by replacing null values or augmenting with derived metrics.

Data Format:
Data will be saved in CSV format for preprocessing and analysis.

Model Development:
Use machine learning regression algorithms (e.g., Random Forest, Neural Networks) to predict player playtime and retention.
Evaluate models using metrics such as mean absolute error (MAE), mean squared error (MSE), and R-squared (R²), particularly focusing on handling potential outliers and variance.

Deployment:
Deploy the model using Streamlit, an interactive platform for building and hosting applications.
Include dynamic components like sliders, dropdown menus, and text inputs for user data entry.
Display visualizations such as retention probability graphs, feature importance charts, and performance metrics.
