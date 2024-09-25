from Extention.speak import *
from Extention.SpeechRecognition import *
from SolarBodieName import *

if __name__ == "__main__":
    startup()
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

     # Logic for executing tasks based on query
        if "number of planets" in query:
            Solarbodiename('name')