import pandas as pd
import streamlit as st
import pickle
import requests
movies_list = pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
  movie_index=movies[movies['title'] == movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
  recommended_movies=[]
  recommended_movie_posters = []
  for i in movies_list[1:6]:

      movie_id = movies.iloc[i[0]].movie_id
      recommended_movie_posters.append(fetch_poster(movie_id))

      recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies,recommended_movie_posters

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
     'Enter Any Movie Name',
    movies['title'].values)



if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.caption(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.caption(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.caption(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.caption(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.caption(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])







