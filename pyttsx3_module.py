import pyttsx3

text = "Hey, This is Py TTSX3 module from python"

engine = pyttsx3.init()
Voices = engine.getProperty("voices")
engine.setProperty("voice", Voices[1].id)# 0 for male voice and 1 for female voice
engine.say(text)
engine.runAndWait()