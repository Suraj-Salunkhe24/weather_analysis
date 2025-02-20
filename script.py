import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1] List of cities and API key
cities = ['New York', 'London', 'Tokyo']
api_key = 'd94238ed7964bac03af5eda1a6c9cf0c'


# 2] Function to get weather data
def get_weather_data(cities):
    weather_data = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            city_name = data['name']
            temperature = data['main']['temp']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            weather_data.append([city_name, temperature, weather, humidity])
        else:
            print(f"Error retrieving data for {city}: {data['message']}")
    return weather_data


# 3] Get weather data Create a DataFrame and Display the DataFrame
weather_data = get_weather_data(cities)
df = pd.DataFrame(weather_data, columns=['City', 'Temperature', 'Weather', 'Humidity'])
print("\n weather_data",df)


# 4]Create a bar chart for temperatures
plt.bar(df['City'], df['Temperature'], color='blue')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.title('Current Temperatures in Cities')
plt.show()

# 5]display the city with the highest and lowest temperatures
highest_temp_city = df.loc[df['Temperature'].idxmax()]
lowest_temp_city = df.loc[df['Temperature'].idxmin()]
print(f"City with highest temperature: {highest_temp_city['City']} ({highest_temp_city['Temperature']}°C)")
print(f"City with lowest temperature: {lowest_temp_city['City']} ({lowest_temp_city['Temperature']}°C)")