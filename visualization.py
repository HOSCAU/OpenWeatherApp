import matplotlib.pyplot as plt

def plot_daily_summary(daily_summaries: list):
    dates = [entry['date'] for entry in daily_summaries]
    avg_temps = [entry['average_temp'] for entry in daily_summaries]
    max_temps = [entry['max_temp'] for entry in daily_summaries]
    min_temps = [entry['min_temp'] for entry in daily_summaries]

    plt.plot(dates, avg_temps, label='Average Temperature')
    plt.plot(dates, max_temps, label='Max Temperature', linestyle='--')
    plt.plot(dates, min_temps, label='Min Temperature', linestyle='--')
    plt.legend()
    plt.title('Daily Weather Summary')
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.xticks(rotation=45)
    plt.show()
