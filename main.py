import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak the message
def speak(message):
    engine.say(message)
    engine.runAndWait()
    



# Function to listen for user's voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Could not request results from the speech recognition service.")
        return ""

# Greet the user
def greet_user():
    speak("Hello, I'm your personal Voice Assistant. How can I help you?")

# Get the current date and time
def tell_date_and_time():
    now = datetime.datetime.now()
    date = now.strftime("%A, %B %d, %Y")
    time = now.strftime("%I:%M %p")
    speak(f"Today's date is {date} and the time is {time}.")

# Open YouTube
def open_youtube():
    speak("What do you want to search on YouTube?")
    query = listen()
    if query:
        search_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(search_url)
        speak(f"Opening YouTube to search for {query}.")

# Search Wikipedia
def search_wikipedia():
    speak("What do you want to search on Wikipedia?")
    query = listen()
    if query:
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Found multiple results, please be more specific. Options: {', '.join(e.options)}")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("Sorry, I am having trouble accessing Wikipedia right now.")

# Open email (Gmail)
def open_email():
    speak("Opening your email.")
    webbrowser.open("https://mail.google.com")

# Open WhatsApp
def open_whatsapp():
    speak("Opening WhatsApp.")
    webbrowser.open("https://web.whatsapp.com")

# Process voice commands
def process_command():
    command = listen()
    if 'youtube' in command:
        open_youtube()
    elif 'wikipedia' in command:
        search_wikipedia()
    elif 'date' in command or 'time' in command:
        tell_date_and_time()
    elif 'email' in command:
        open_email()
    elif 'whatsapp' in command:
        open_whatsapp()
    elif 'close' in command or 'exit' in command:
        speak("Goodbye!")
        root.destroy()
    else:
        speak("Sorry, I didn't understand that command.")
        

# GUI Design
def create_gui():
    global root
    root = tk.Tk()
    root.title(" Automated Voice Assistant By Saurav Kumar")
    root.geometry("400x600")
    root.resizable(False, False)

    # Load background image
    background_image = Image.open("jarvis.png")
    background_image = background_image.resize((400, 600),)
    bg_image = ImageTk.PhotoImage(background_image)

    # Create a label for the background image
    background_label = tk.Label(root, image=bg_image)
    background_label.place(relwidth=1, relheight=1)

    # Title
    title = tk.Label(root, text="Voice Assistant", font=("Arial", 20, "bold"), bg="#000000", fg="#FFFFFF")
    title.pack(pady=10)

    # Task buttons
    tasks_frame = tk.Frame(root, bg="#000000")
    tasks_frame.pack(pady=20)

    btn_youtube = tk.Button(tasks_frame, text="Open YouTube", width=20, command=open_youtube)
    btn_youtube.grid(row=0, column=0, padx=10, pady=10)

    btn_whatsapp = tk.Button(tasks_frame, text="Open WhatsApp", width=20, command=open_whatsapp)
    btn_whatsapp.grid(row=0, column=1, padx=10, pady=10)

    btn_email = tk.Button(tasks_frame, text="Open Email", width=20, command=open_email)
    btn_email.grid(row=1, column=0, padx=10, pady=10)

    btn_datetime = tk.Button(tasks_frame, text="Date and Time", width=20, command=tell_date_and_time)
    btn_datetime.grid(row=1, column=1, padx=10, pady=10)

    btn_wikipedia = tk.Button(tasks_frame, text="Search Wikipedia", width=20, command=search_wikipedia)
    btn_wikipedia.grid(row=2, column=0, columnspan=2, pady=10)

    # Speak button
    speak_button = tk.Button(root, text="Speak", font=("Arial", 16), bg="blue", fg="white", command=process_command)
    speak_button.pack(pady=20, ipadx=20, ipady=10)

    # Close button
    close_button = tk.Button(root, text="Close Window", command=root.destroy, bg="red", fg="white")
    close_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    greet_user()
    create_gui()
