#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Displaying commute time
"""

from config.demo_opts import get_device
from luma.core.render import canvas
import urllib.request
import json
from config.config import api_key, destination, origin, mode
import threading
from datetime import datetime, timedelta

google_api_endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
query_string_params = 'origin={}&destination={}&mode={}&key={}'.format(
    origin, destination, mode, api_key)
request_url = google_api_endpoint + query_string_params

# Writing to the screen


def get_updated_commute():
    api_response = urllib.request.urlopen(request_url).read()
    returned_directions = json.loads(api_response)
    commute_time = returned_directions['routes'][0]['legs'][0]['duration']['text']
    return commute_time


def write_to_screen(minutes_to_wait):
    time_at_start = datetime.now()
    refresh_time = time_at_start + timedelta(minutes=1)
    commute_time = get_updated_commute()
    while True:
        if (datetime.now() > refresh_time):
            refresh_time = datetime.now() + timedelta(minutes=minutes_to_wait)
            print('updating commute')
            commute_time = get_updated_commute()
        with canvas(device) as draw:
            margin = 2
            x_axis = 2
            y_axis = min(device.height, 64) / 2
            draw.text((2 * (x_axis + margin), y_axis - 20),
                      'Time to Get Home:', fill="yellow")
            draw.text((2 * (x_axis + 90 + margin), y_axis - 20),
                      commute_time, fill="yellow")


def main(minutes_to_wait):
    write_to_screen(minutes_to_wait)


if __name__ == "__main__":
    try:
        minutes_to_wait = input('How many minutes between commute refresh? \n')
        device = get_device()
        main(int(minutes_to_wait))
    except KeyboardInterrupt:
        pass
