print(" welcome to Weather app 1.1 by vani narwani.")
import requests
city=input("please enter your city :")
URL=f"http://api.weatherapi.com/v1/current.json?key=e2025daca499485dbdd73017230506&q={city}"
    
  
r=requests.get(URL)
print(r.text)
import os
os.system("start weather.mp3")