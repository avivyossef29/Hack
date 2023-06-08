import math
import requests

class user:
    __in

def get_travel_time(origin, destination, mode='driving'):
    api_key = 'AIzaSyCfZUFEceP68o8cF06J0gVYoZraZ5ET9bw'  # Replace with your Google Maps API key
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    params = {
        'origins': origin,
        'destinations': destination,
        'mode': mode,
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        duration_sec = data['rows'][0]['elements'][0]['duration']['value']
        return math.floor(duration_sec/60)
    else:
        print('Error occurred.')
    return duration



