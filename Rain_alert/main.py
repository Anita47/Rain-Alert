import requests

from twilio.rest import Client 

api_key='69f04e4613056b159c2761a9d9e664d2'
OWN_Endpoint="https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'ACcee0c167d1650b1eb86f00daf2e22179'
auth_token = '21e6f234eac9966c2ec87b0941f3243e'

weather_params={
    "lat":28.408913,
    "lon":77.317787,
    "appid":api_key,
    "exclude":"current,minutley,daily",
    }



response=requests.get(OWN_Endpoint,params=weather_params)
response.raise_for_status()

weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False
for hour_data in weather_slice:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client=Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂",
                     from_='+12342241648',
                     to='+917982662745'
             )

    print(message.status)

