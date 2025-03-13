import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import requests

# Initialize Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  

def speak(text):
    """Make Jarvis speak"""
    engine.say(text)
    engine.runAndWait()

def recognize_command():
    """Recognize voice commands from a distance"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Improves recognition
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please speak clearly.")
        return ""
    except sr.RequestError:
        speak("Could not request results, please check your connection.")
        return ""

def get_weather():
    """Fetch Weather Details"""
    API_KEY = "your_api_key_here"
    CITY = "Islamabad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        weather_desc = response["weather"][0]["description"]
        speak(f"The temperature is {temp} degrees with {weather_desc}")
    except:
        speak("Sorry, I couldn't fetch the weather.")

def add_new_project():
    """Create a new project file in the websites folder and open it"""
    speak("What should be the name of the new file?")
    file_name = recognize_command()
    if file_name:
        file_path = os.path.join("C:\\Users\\HP\\Desktop\\websites", file_name)
        with open(file_path, "w") as file:
            file.write("<!-- New Project File Created -->")
        speak(f"File {file_name} has been created and opening it now.")
        os.startfile(file_path)
    else:
        speak("File name not recognized.")

def execute_command(command):
    """Execute Commands"""

    # 🔹 Web Commands
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp Web")

    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")

    elif "open stack overflow" in command:
        webbrowser.open("https://stackoverflow.com")
        speak("Opening Stack Overflow")
    elif "open python tutorial" in command:
        webbrowser.open("https://www.youtube.com/watch?v=ERCMXc8x7mc&t=32173s")
        speak("opening python tutorial")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching {search_query} on Google")

    elif "weather" in command:
        get_weather()

    # 🔹 System Control
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 5")

    elif "lock screen" in command:
        speak("Locking the screen.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    # 🔹 Productivity & Developer Tools
    elif "open vs code" in command:
        os.startfile(r"C:\Users\HP\Desktop\Professional Websites\Code.exe")
        speak("Opening VS Code")

    elif "run python script" in command:
        speak("Which script should I run?")
        script_name = recognize_command() + ".py"
        os.system(f"python {script_name}")
        speak(f"Running {script_name}")

    elif "add a new project to my websites folder" in command:
        add_new_project()

    # 🔹 Time & Date
    elif "what is time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "what is date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    # 🔹 Random AI Chatting
    elif "how are you" in command:
        speak("I am just a virtual assistant, but I am doing great!")

    elif "who created you" in command:
        speak("I was created by Mohammad, the coding master!")

    elif "who am i" in command:
        speak("You are my master, Mohammad!")

    elif "are you real" in command:
        speak("I am as real as the internet!")

    elif "do you love me" in command:
        speak("I love helping you, Mohammad!")

    elif "what is your name" in command:
        speak("I am Jarvis, your AI assistant!")

    elif "jarvis deactivate" in command or "deactivate" in command:
        speak("Jarvis deactivated")
        exit()

    elif "jarvis" in command:
        speak("Yes Sir, I am listening")

    elif "thanks" or "thank you" in command:
        speak("Your Welcome Sir")
    else:
        speak("Command not recognized.")

if __name__ == "__main__":
    speak("Jarvis activated. How can I assist you?")
    while True:
        command = recognize_command()
        if command:
            execute_command(command)