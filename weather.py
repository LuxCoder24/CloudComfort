def getWeather(lat, lon):
  
    import requests

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,precipitation,cloud_cover"

    r = requests.get(url)

    data = r.json()

    temp = data['current']['temperature_2m']
    perc = data['current']['precipitation']
    cloud = data['current']['cloud_cover']

    return temp, perc, cloud

