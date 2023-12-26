import requests
from datetime import datetime

MY_LAT = 33.307575
MY_LNG = -111.844940

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # Need to understand and properly respond to different network codes: 1xx 2xx 3xx 4xx 5xx
# response.raise_for_status()
# # store data on variable to display content
# data = response.json()
# # access and store longitude and latitude respectably
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# # Store it in a tuple
# iss_poisition = (latitude, longitude)

# print(iss_poisition)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # toggles 12 hour format to 24 hour format, toggle back with value : 1
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # We split by the letter T into a 2 item list and further split it by index 1
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
