import requests
from datetime import datetime
import os

APP_ID = "your_API_ID"
APP_KEY = "your_API_KEY"
USERNAME = "Your_username"

nutritionix_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
parameters = {
    "query": input("enter the exercise you had today ?")
}
nutritionix_response = requests.post(url=nutritionix_end_point, json=parameters, headers=nutritionix_header)
data = nutritionix_response.json()["exercises"][0]
exercise = data["user_input"].title()
duration = data["duration_min"]
calories = data["nf_calories"]

post_endpoint = f"https://api.sheety.co/{username}/myWorkout/workouts"
date_time = datetime.now()
date = date_time.strftime(f"%d/%m/%Y")
time = date_time.strftime("%T")
post_parameters = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
post_response = requests.post(url=post_endpoint, json=post_parameters)

authentication_header = {
    "Authorization": "Basic (your_Authentication_code)"
}
authentication_response = requests.post(post_endpoint, json=post_parameters, headers=authentication_header)
print(authentication_response.text)
