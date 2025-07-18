# importing important libraries
import streamlit as st
import urllib.request
import pickle
import pandas as pd
import requests
import json


# defining the variable API KEY -- which will be used to fetch data from TMDb
API_KEY='61aba20f1124c5b0a9f6abd52e32402c'


# defining function to fetch poster using movie-id
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"


    # fetch data from API in JSON form
    response=requests.get(url)
    data=response.json()
    # return image
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']


# defining function which will fetch movies names and their posters using the API Key
def recommend(movie):
    movie_index=movies[movies['title_x']==movie].index[0]
    distances=similarity[movie_index]
    movies_list1=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_list1:
        movies_id=movies.iloc[i[0]].id

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movies_id))
        recommended_movies.append(movies.iloc[i[0]].title_x)

    return recommended_movies,recommended_movies_posters


# import movies DataFrame using pickle library
movies_list=pickle.load(open('movie_dict.pkl','rb'))


# converting the data to pandas dataframe
movies=pd.DataFrame(movies_list)


# import similarity matrix using pickle
similarity=pickle.load(open('similarity.pkl','rb'))


# define Title
st.title("Movie Recommender System")


# define selectBox
selected_movie=st.selectbox('Select Movie',
                    movies['title_x'].values)


# defining Recommend button
if st.button('Recommend'):
    names,poster=recommend(selected_movie)

    # defining columns to display recommended movies
    col1,col2,col3,col4,col5 = st.columns(5)

    # Here one columns consists of title(st.text) and movie poster(in poster[])
    with col1:
        st.text(names[0])
        st.image(poster[0])


    with col2:
        st.text(names[1])
        st.image(poster[1])



    with col3:
        st.text(names[2])
        st.image(poster[2])


    with col4:
        st.text(names[3])
        st.image(poster[3])


    with col5:
        st.text(names[4])
        st.image(poster[4])