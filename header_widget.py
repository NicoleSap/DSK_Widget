import tkinter as tk

def create_header(root):
    # Function to close the application
    def close_app():
        root.destroy()

    # Function to minimize the application
    def minimize_app():
        root.overrideredirect(False)  # Temporarily disable override-redirect
        root.iconify()  # Minimize the application
        root.overrideredirect(True)  # Re-enable override-redirect when restored

    # Create the header
    header_label = tk.Label(root, text="Weather", bg="#cdb4db", fg="white", font="Arial", anchor="w")
    header_label.pack(fill=tk.X)

    # Create a frame for the buttons (to place them on the right)
    button_frame = tk.Frame(root, bg="#cdb4db")  # Matches the header's background
    button_frame.place(relx=1.0, rely=0.0, anchor="ne")  # Place the frame at the top-right corner

    # Create the Settings button
    settings_button = tk.Button(button_frame, text="⚙", bg="#cdb4db", fg="white", font=("Arial", 12), borderwidth=0)
    settings_button.pack(side=tk.LEFT, padx=(0, 5))  # Pack to the left with some spacing

    # Create the Minimize button
    minimize_button = tk.Button(button_frame, text="-", bg="#cdb4db", fg="white", font=("Arial", 12), borderwidth=0, command=minimize_app)
    minimize_button.pack(side=tk.LEFT, padx=(0, 5))

    # Create the Close button
    close_button = tk.Button(button_frame, text="X", bg="#cdb4db", fg="white", font=("Arial", 12), borderwidth=0, command=close_app)
    close_button.pack(side=tk.LEFT)