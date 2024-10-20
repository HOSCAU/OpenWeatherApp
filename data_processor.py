from datetime import datetime


class WeatherDataProcessor:
    @staticmethod
    def kelvin_to_celsius(kelvin_temp: float) -> float:
        return kelvin_temp - 273.15

    @staticmethod
    def get_daily_summary(weather_data: list):
        # Check if weather_data is not empty
        if not weather_data:
            print("No weather data available.")
            return None

        temps = [entry['main']['temp'] for entry in weather_data if 'main' in entry and 'temp' in entry['main']]

        if len(temps) == 0:
            print("No temperature data available.")
            return None

        # Convert temperatures to Celsius
        temps_celsius = [WeatherDataProcessor.kelvin_to_celsius(temp) for temp in temps]

        average_temp = sum(temps_celsius) / len(temps_celsius)
        max_temp = max(temps_celsius)
        min_temp = min(temps_celsius)
        main_conditions = [entry['weather'][0]['main'] for entry in weather_data if 'weather' in entry]

        dominant_condition = max(set(main_conditions), key=main_conditions.count)

        return {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'average_temp': average_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }

# Example usage
# weather_data = [...]  # This should be the actual weather data you retrieve from the API
# summary = WeatherDataProcessor.get_daily_summary(weather_data)
# print(summary)
