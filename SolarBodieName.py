from speak import *
import requests

def Solarbodiename(Number):
    
    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    r = requests.get(url)

    Data = r.json()

    bodies = Data['bodies']

    Number = len(bodies)

    speak(f"Number of planets in solar system : {Number}.")

    for bodyy in bodies:

        speak(bodyy['id'],end=',')

Solarbodiename()        