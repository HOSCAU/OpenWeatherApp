weather_data = [
    {'main': {'temp': 300.2}, 'weather': [{'main': 'Haze'}]},
    {'main': {'temp': 301.5}, 'weather': [{'main': 'Clear'}]},
    {'main': {'temp': 299.0}, 'weather': [{'main': 'Haze'}]}
]

summary = WeatherDataProcessor.get_daily_summary(weather_data)
print(summary)
