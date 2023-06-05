#Create a command-line tool that accepts a city's name and returns the current 
#weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it 
#using Python. Your solution should demonstrate how GitHub Copilot can help you 
#with API usage, data parsing, and error handling.

#Importing the necessary libraries
import requests
import sys

#API key
API_KEY = "2aa1ece3b8fbe8d51df36e1d7ad22faa"

#Function to get the weather data
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
#Function to parse the weather data
def parse_weather(weather_data):
    if weather_data is None:
        return None
    else:
        weather = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        return {"weather": weather, "temp": temp, "feels_like": feels_like, "humidity": humidity, "wind_speed": wind_speed}
    
#Function to print the weather data
def print_weather(weather_data):
    if weather_data is None:
        print("City not found")
    else:
        print(f"Current weather: {weather_data['weather']}")
        print(f"Temperature: {weather_data['temp']} K")
        print(f"Feels like: {weather_data['feels_like']} K")
        print(f"Humidity: {weather_data['humidity']} %")
        print(f"Wind speed: {weather_data['wind_speed']} m/s")

#Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <city>")
        sys.exit(1)
    else:
        city = sys.argv[1]
        weather_data = get_weather(city)
        weather_data = parse_weather(weather_data)
        print_weather(weather_data)

if __name__ == "__main__":
   main()