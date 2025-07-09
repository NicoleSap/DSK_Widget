import requests
import tkinter as tk

# Function to get the weather from an API
def get_weather(api_key, city="New York"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
        response = requests.get(url)
        weather_data = response.json()

        if response.status_code == 200:
            temp = weather_data['main']['temp']  # Current temperature
            description = weather_data['weather'][0]['description']  # Weather description
            print(get_weather(api_key, city))
            return f"{city}: {temp}°F, {description.capitalize()}"
        else:
            return "Unable to fetch weather data."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to add the weather display to the Tkinter app
def create_weather_widget(root, api_key, city="New York"):
    weather_label = tk.Label(root, text=get_weather(api_key, city), bg="#cdb4db", fg="white", font=("Arial", 12))
    weather_label.pack(side=tk.TOP, pady=10)  # Place it at the bottom of the window