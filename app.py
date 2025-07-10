import os
import requests
import sys
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("WEATHER_API")
CITY = 'New York'
UNITS = 'metric' 

# Create the application object
app = QApplication(sys.argv)

# Create a basic window
window = QWidget()
window.setWindowTitle('Cute Companion App')
window.setGeometry(100, 100, 300, 300)  # x, y, width, height



# Create the time label
time_label = QLabel(parent=window)
time_label.move(200, 0)  # Adjust based on your window size
time_label.resize(90, 20)

# Function to update the time
def update_time():
    current_time = QTime.currentTime().toString('h:mm AP')
    time_label.setText(current_time)
# Timer to refresh the time every second
timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)
update_time()  # Initial call

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={api_key}&units={UNITS}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"{int(temp)}°C, {desc.capitalize()}"
    else:
        return "Weather error"

# Create and place weather label
weather_label = QLabel(parent=window)
weather_label.move(10, 10)
weather_label.resize(200, 20)
weather_label.setText(get_weather())


# Show the window
window.show()

# Run the application's event loop
sys.exit(app.exec_())
