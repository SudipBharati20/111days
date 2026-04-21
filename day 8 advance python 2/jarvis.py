
# File: jarvis.py
# MEGA PROJECT 1: JARVIS - Voice Activated Virtual Assistant

"""
Q: Create a voice-activated virtual assistant (Jarvis) that can:
- Listen to voice commands
- Open websites
- Play music
- Fetch news
- Respond using AI (GPT-3.5-turbo)
"""

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
from gtts import gTTS
import pygame
import os

# ---------------- TEXT TO SPEECH ---------------- #

engine = pyttsx3.init()

def speak(text):
    """Convert text to speech using pyttsx3"""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- WAKE WORD LISTENER ---------------- #

def listen_command():
    """Listen for voice command"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        return ""

# ---------------- AI RESPONSE (OPENAI) ---------------- #

def ai_response(query):
    """Get response from OpenAI GPT model"""

    openai.api_key = "YOUR_OPENAI_API_KEY"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )

    return response["choices"][0]["message"]["content"]

# ---------------- NEWS FUNCTION ---------------- #

def get_news():
    """Fetch latest news using NewsAPI"""

    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    articles = data["articles"]

    for i, article in enumerate(articles[:5]):
        speak(f"News {i+1}: {article['title']}")

# ---------------- MAIN JARVIS ---------------- #

if __name__ == "__main__":

    speak("Initializing Jarvis...")

    while True:

        command = listen_command()

        if "jarvis" in command:
            speak("Ya")

            command = listen_command()

            # ---------------- WEB BROWSING ---------------- #
            if "open google" in command:
                webbrowser.open("https://google.com")

            elif "open youtube" in command:
                webbrowser.open("https://youtube.com")

            elif "open facebook" in command:
                webbrowser.open("https://facebook.com")

            elif "open linkedin" in command:
                webbrowser.open("https://linkedin.com")

            # ---------------- MUSIC ---------------- #
            elif command.startswith("play"):
                song = command.split(" ")[1]
                link = musicLibrary.music[song]
                webbrowser.open(link)

            # ---------------- NEWS ---------------- #
            elif "news" in command:
                get_news()

            # ---------------- AI RESPONSE ---------------- #
            else:
                response = ai_response(command)
                speak(response)