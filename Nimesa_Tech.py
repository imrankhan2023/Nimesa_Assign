# Import the necessary libraries
import requests

# Replace 'your_api_url' with the actual URL of the API endpoint
API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'

# Function to get weather data for a specific date
def get_weather_data(date):
    response = requests.get(f"{API_URL}/weather", params={'date': date})
    data = response.json()
    return data['temperature']

# Function to get wind speed data for a specific date
def get_wind_speed_data(date):
    response = requests.get(f"{API_URL}/wind_speed", params={'date': date})
    data = response.json()
    return data['wind_speed']

# Function to get pressure data for a specific date
def get_pressure_data(date):
    response = requests.get(f"{API_URL}/pressure", params={'date': date})
    data = response.json()
    return data['pressure']

# Main program loop
while True:
    print("Options:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        date = input("Enter the date (dd/mm/yyyy): ")
        temperature = get_weather_data(date)
        print(f"Temperature on {date}: {temperature}°C\n")
    elif option == '2':
        date = input("Enter the date (YYYY-MM-DD): ")
        wind_speed = get_wind_speed_data(date)
        print(f"Wind speed on {date}: {wind_speed} km/h\n")
    elif option == '3':
        date = input("Enter the date (YYYY-MM-DD): ")
        pressure = get_pressure_data(date)
        print(f"Pressure on {date}: {pressure} hPa\n")
    elif option == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.\n")