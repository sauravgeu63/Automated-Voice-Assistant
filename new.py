import tkinter as tk
from tkinter import PhotoImage

# Function to display the speak action
def on_speak():
    # Create a microphone icon (you can download a PNG image of a microphone or use any icon)
    mic_icon = PhotoImage(file="jarvis.png")  # Make sure to place a mic_icon.png in the directory or provide a path
    mic_label.config(image=mic_icon)
    mic_label.image = mic_icon
    speak_label.config(text="Speak Now!")

# Function to close the window
def close_window():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Speak and Close GUI")

# Create the Speak button
speak_button = tk.Button(root, text="Speak", command=on_speak)
speak_button.pack(pady=10)

# Label to display the "Speak Now" text
speak_label = tk.Label(root, text="", font=("Helvetica", 14))
speak_label.pack(pady=10)

# Label to display the microphone icon (initially empty)
mic_label = tk.Label(root)
mic_label.pack(pady=10)

# Create the Close button
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack(pady=10)

# Run the application
root.mainloop()
