import streamlit as st
from weather import getWeather
from cities import getlatlon

tabs = ["Home", "Other"]

tab0, tab1= st.tabs(tabs)

tab0.title("Where will your dreams take you?")

input_col1, input_col2 = tab0.columns(2)

# Name of the city
city = input_col1.text_input("City:")

# Name of the country - needed to make sure that the city is in the correct country
country = input_col2.text_input("Country:")


######################################### Weather #############################################
if tab0.button("Go"):

    # Using the 'cities' script to find the latitude and longitude
    lat, lon = getlatlon(city, country)

    # Getting live weather
    temp, perc, cloud = getWeather(lat, lon)


    wether_col1, weather_col2, weather_col3 = tab0.columns(3)

    wether_col1.metric("Temperature", f"{temp}°C")
    weather_col2.metric("Percipitation", f"{perc}%")
    weather_col3.metric("Cloud covrage", f"{cloud}%")