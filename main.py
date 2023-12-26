import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Need to understand and properly respond to different network codes: 1xx 2xx 3xx 4xx 5xx
response.raise_for_status()
# store data on variable to display content
data = response.json()
# access and store longitude and latitude respectably
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Store it in a tuple
iss_poisition = (latitude, longitude)

print(iss_poisition)
