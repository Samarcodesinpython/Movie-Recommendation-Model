import streamlit as st
import pandas as pd
import pickle
import requests

# Fetch poster using movie ID
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2542c862ca7c2bf63c7ea3c49f537927&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
    return full_path

# Recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Load data
movies_dict = pickle.load(open('Pickle/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('Pickle/similarity.pkl', 'rb'))

# Streamlit App
st.title('🎬 Movie Recommendation System')

st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
    }
    .movie-title {
        font-size: 20px; 
        font-weight: bold; 
        text-align: center; 
        color: grey;
        overflow: hidden; 
        text-overflow: ellipsis;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


selected_movie_name = st.selectbox(
    "🎥 Select a Movie to Get Recommendations:",
    movies['title'].values
)

if st.button('Show Recommendations'):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    for i in range(0, len(recommended_movies), 4):
        cols = st.columns(4, gap="small")
        for col, movie_name, poster_url in zip(cols, recommended_movies[i:i+5], recommended_posters[i:i+5]):
            with col:
                if poster_url:
                    st.image(poster_url, width=195, caption="")
                st.markdown(
                    f'<div class="movie-title tooltip" title="{movie_name}">{movie_name}</div>',
                    unsafe_allow_html=True,
                )
