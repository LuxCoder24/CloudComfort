import streamlit as st
from weather import getWeather

tabs = ["Home", "Other"]

tab0, tab1= st.tabs(tabs)


tab0.title("Weather")
lat = tab0.text_input("Latitude: ")
lon = tab0.text_input("Longitude: ")

if tab0.button("Go"):
    # Writing the weather on the page
    temp, snow, cloud = getWeather(lat, lon)
    tab0.write(f"Temperature: {temp}C")
    tab0.write(f"Snow coverage: {snow}")
    tab0.write(f"Cloud cover: {cloud}")