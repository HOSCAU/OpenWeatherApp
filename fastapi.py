from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/weather")
async def get_weather(city: str):
    api_key = "b3a444c84bb110dbcfada5928562a9bd"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")

    return response.json()
