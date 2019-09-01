from luma.core.render import canvas
import urllib.request
import json
from config.config import api_key, destination, origin, mode, color, option_2_minutes_offset, option_3_minutes_offset
from time import time
import math

google_api_endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
time_at_start = time()
margin = 2
x_axis = 2
y_axis = 32


def minutes_to_seconds(minutes):
    return minutes * 60


def get_updated_commute(departure_time):
    query_string_params = 'origin={}&destination={}&mode={}&departure_time={}&key={}'.format(
        origin, destination, mode, math.floor(departure_time), api_key)
    request_url = google_api_endpoint + query_string_params
    api_response = urllib.request.urlopen(request_url).read()
    returned_directions = json.loads(api_response)
    commute_time = returned_directions['routes'][0]['legs'][0]['duration']['text']
    return commute_time


def draw_row(display_text, commute_time, draw, offset_y):
    draw.text((2 * (x_axis + margin), y_axis - offset_y),
              display_text, fill=color)
    draw.text((2 * (x_axis + 90 + margin), y_axis - offset_y),
              commute_time, fill=color)


def write_to_screen(minutes_to_wait, device):
    refresh_time = time_at_start + minutes_to_seconds(minutes_to_wait)
    # Defining the times at the start
    leaving_now_commute_time = get_updated_commute(time())
    time_plus_option_2_minutes = time() + minutes_to_seconds(option_2_minutes_offset)
    time_plus_option_3_minutes = time() + minutes_to_seconds(option_3_minutes_offset)

    option_2_commute_time = get_updated_commute(
        time_plus_option_2_minutes)
    option_3_commute_time = get_updated_commute(
        time_plus_option_3_minutes)
    while True:
        if (time() > refresh_time):
            # Refreshing the times
            refresh_time = time() + minutes_to_seconds(minutes_to_wait)
            time_plus_option_2_minutes = time() + minutes_to_seconds(option_2_minutes_offset)
            time_plus_option_3_minutes = time() + minutes_to_seconds(option_3_minutes_offset)
            # Refreshing the commutes
            leaving_now_commute_time = get_updated_commute(time())
            option_2_commute_time = get_updated_commute(
                time_plus_option_2_minutes)
            option_3_commute_time = get_updated_commute(
                time_plus_option_3_minutes)
            print('updating commute')
        with canvas(device) as draw:
          # offset_y: the higher the number the higher the text
            draw_row('Commute - Leaving Now:',
                     leaving_now_commute_time, draw, 25)
            draw_row('Commute - Leaving in 20 min:',
                     option_2_commute_time, draw, 8)
            draw_row('Commute - Leaving in 1 hr',
                     option_3_commute_time, draw, (0 - 10))
