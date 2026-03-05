import requests
from twilio.rest import Client
import os
print(os.environ.get("LAT", "MISSING"))

account_sid = os.environ.get("TWI_SID")
auth_token = os.environ.get("TWI_TOKEN")
API_KEY = os.environ.get("OWM_KEY")
URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = 36.36576025716617
LONG = -117.00230704760706



params = {
    "lat" :  36.36576025716617,
    "lon" : -117.00230704760706,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(URL, params = params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

will_rain = False
for hr_data in weather_data["list"]:
    weather_condition = hr_data["weather"]
    id_code = weather_condition[0]["id"]
    if id_code > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_= os.environ.get("TWI_FROM"),
      body = "bring an umbrella, nerd ☔️",
      to = os.environ.get("TWI_TO")
    )
    print(message.body)

else:
    print("sunny skies")
