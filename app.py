import streamlit as st
import pandas as pd

movies = pd.read_csv('movies.csv')

def recommend_movies(movie_name, n=5):
    if movie_name not in movies['title'].values:
        return ["Movie not found!"]
    return movies.sample(n)['title'].values

st.title("🎬 Movie Recommendation System")
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button("Recommend"):
    st.subheader("🍿 Top 5 Similar Movies:")
    result = recommend_movies(selected_movie)
    for i, movie in enumerate(result, 1):
        st.write(f"{i}. 🎥 {movie}")