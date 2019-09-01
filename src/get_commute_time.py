import urllib.request
import json
from config.config import api_key, destination, origin, mode
import threading

google_api_endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
query_string_params = 'origin={}&destination={}&mode={}&key={}'.format(
    origin, destination, mode, api_key)
request_url = google_api_endpoint + query_string_params

# Writing to the screen


def get_updated_commute():
    api_response = urllib.request.urlopen(request_url).read()
    returned_directions = json.loads(api_response)
    commute_time = returned_directions['routes'][0]['legs'][0]['duration']['text']

    print(commute_time)


def set_interval(function_to_run, interval_time_in_minutes):
    e = threading.Event()
    # Formatting variables
    seconds_to_wait = interval_time_in_minutes * 60
    minutes_display = 'minute' if interval_time_in_minutes == 1 else 'minutes'
    print('Fetching fresh commute every {} {}'.format(interval_time_in_minutes,
                                                      minutes_display))
    # Running the function before setting interval ( on initial call )
    function_to_run()
    while not e.wait(seconds_to_wait):
        function_to_run()
