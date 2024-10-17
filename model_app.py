import joblib
import streamlit as st

model = joblib.load("regression.joblib")

size = st.number_input("size")
nb_bedrooms = st.number_input("nb_bedrooms")
garden = st.number_input("garden")


st.write(model.predict([[size, nb_bedrooms, garden]]))