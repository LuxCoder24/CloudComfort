import streamlit as st
from weather import getWeather
from cities import getlatlon

tabs = ["Home", "Other"]

tab0, tab1= st.tabs(tabs)


tab0.title("Weather")

# Name of the city
city = tab0.text_input("Enter the city name: ")

# Name of the country - needed to make sure that the city is in the correct country
country = tab0.text_input("Enter the country name: ")


if tab0.button("Go"):

    lat, lon = getlatlon(city, country)

    temp, perc, cloud = getWeather(lat, lon)

    tab0.write(f"Lattitude: {lat} ")
    tab0.write(f"Longitude: {lon} ")
               
    tab0.write(f"Temperature: {temp}C")
    tab0.write(f"Percipitation: {perc}")
    tab0.write(f"Cloud cover: {cloud}")