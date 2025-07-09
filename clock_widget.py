import tkinter as tk
from time import strftime
from PIL import ImageFont, Image, ImageTk, ImageDraw  # Import additional modules
from header_widget import create_header
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
from weather_widget import create_weather_widget

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("clock_widget.py"):
            os.execv(sys.executable, ['python'] + sys.argv)

# Set up the observer
event_handler = ReloadHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()

def update_time():
    current_time = strftime('%I:%M %p').lstrip('0')  # Removes the leading zero manually
    

    image = Image.new("RGB", (370, 370), "#cdb4db")
    draw = ImageDraw.Draw(image)
    draw.text((20, 25), current_time, font=custom_font, fill="#ffc8dd") 
    

    time_image = ImageTk.PhotoImage(image)
    time_label.config(image=time_image)
    time_label.image = time_image  # Keep a reference to prevent garbage collection
    
    time_label.after(1000, update_time)  # Update every second

# Functions to allow dragging the window
def start_move(event):
    root.x = event.x
    root.y = event.y

def on_drag(event):
    x_offset = event.x - root.x
    y_offset = event.y - root.y
    root.geometry(f"+{root.winfo_x() + x_offset}+{root.winfo_y() + y_offset}")



# Create the main application window
root = tk.Tk()
root.title("Kat's Widget")
root.geometry("370x370")
root.resizable(False, False)
root.configure(bg="black")


# Bind mouse actions for moving the window
root.bind("<Button-1>", start_move)  # Left mouse button pressed
root.bind("<B1-Motion>", on_drag)   # Mouse movement while left button is held
# Load the custom font
custom_font = ImageFont.truetype("PixelifySans-VariableFont_wght.ttf", size=40) 
create_header(root)

root.overrideredirect(True) 
# Create a label to display the time as an image
time_label = tk.Label(root)
time_label.pack(expand=True)
root.attributes("-topmost", True)
# Start updating the time
update_time()

#weather
api_key = "2bab9b95259559ba1478c84841528b34" 
create_weather_widget(root, api_key, city="New York")



# Start the Tkinter event loop
root.mainloop()
observer.stop()
observer.join()