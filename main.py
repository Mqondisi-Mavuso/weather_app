# Day 35 of 100
# Rain notification app

import os
import requests
from twilio.rest import Client

LATITUDE = "23.901498"
LONGITUDE = "121.545543"

twilio_api_key = "1dfdbce83d8a64bd5cff74a68cd11421"
twilio_account_sid = "ACbcf14bb937f2aaed3e59cf43cca9340d"
twilio_auth_token = "65cbcad85db4b987c28b2e4d693ccf09"
twilio_number = "+19302122954"
twilio_recovery_code = "lTGyyU2nftGITYcFiSV9xFv8ESYV8-ClDGKhoIK_"

twilio_parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()                             # for raising an exception just in case we get wrong http code
weather_data = response.json()

twelve_h_list = weather_data["hourly"][0:12]
weather_id_list = []
for i in range(0, 12):
    weather_id_list.append(twelve_h_list[i]["weather"][0]["id"])        # getting the weather id for the next 12 hours

will_rain = False
for id in weather_id_list:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Mqondisi, It is going to rain today remember to bring an umbrella ☂️!",
        from_=twilio_number,
        to='+8860988030913'
    )

    print(message.sid)