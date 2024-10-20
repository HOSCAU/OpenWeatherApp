import requests

# OpenWeatherMap API URL and key
api_key = 'b3a444c84bb110dbcfada5928562a9bd'  # Replace with your OpenWeatherMap API key
city = 'Berlin'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    weather_data = response.json()
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}K")
    print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print(f"Failed to get weather data. Status code: {response.status_code}")
