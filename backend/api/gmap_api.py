from flask import current_app
import requests

def make_api_call(api_key, long, lat):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f'{long}, {lat}',  # Replace with your desired latitude and longitude
        'radius': '1500',
        'key': api_key,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle error
        return None