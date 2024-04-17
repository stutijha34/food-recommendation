import streamlit as st
import pickle
import pandas as pd


def recommend(foods):
    food_index = foods[foods['name'] == 'food']
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_food = []
    for i in food_list:
        recommend_food.append(food.iloc[i[0]].name)
        return recommend_food


food_dict = pickle.load(open('food_dict.pkl', 'rb'))
food = pd.DataFrame(food_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Food Recommender System")
selected_food_name = st.selectbox("what would like to eat??", food['name'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_food_name)
    for i in recommendations:
        st.write(i)
