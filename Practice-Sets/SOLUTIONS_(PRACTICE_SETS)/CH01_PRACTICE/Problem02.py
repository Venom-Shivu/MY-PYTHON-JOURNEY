# Write a program to use an external module (e.g., `pyttsx3`) to perform an action (like text-to-speech).


import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Shivansh Yadav! How are you")
engine.runAndWait()
# The above module plays the audio i.e Text To Speech(TTS).
# Also this doesn't require an internet connection to work just type a 