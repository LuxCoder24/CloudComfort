import requests
import streamlit as st

tabs = ["Home", "Other"]

tab0, tab1= st.tabs(tabs)

lat = 49.75
lon = 6.17

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,snow_depth,cloud_cover,wind_speed_10m"

r = requests.get(url)

print(r)

data = r.json()

temp = data['hourly']['temperature_2m'][0]
snow = data['hourly']['snow_depth'][0]
cloud = data['hourly']['cloud_cover'][0]

tab0.title("Test")
tab0.write(f"Temperature: {temp}C")
tab0.write(f"Snow coverage: {snow}")
tab0.write(f"Cloud cover: {cloud}")
