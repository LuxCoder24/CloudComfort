def getWeather(lat, lon):
    import requests

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,snow_depth,cloud_cover,wind_speed_10m"

    r = requests.get(url)

    data = r.json()

    temp = data['hourly']['temperature_2m'][0]
    snow = data['hourly']['snow_depth'][0]
    cloud = data['hourly']['cloud_cover'][0]

    return temp, snow, cloud