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
    time_at_start = datetime.now()
    refresh_time = time_at_start + timedelta(minutes=1)
    print(time_at_start)
    print(refresh_time)


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


def main(minutes_to_wait):
    set_interval(get_updated_commute, minutes_to_wait)


if __name__ == "__main__":
    try:
        minutes_to_wait = input('How many minutes between commute refresh? \n')
        device = get_device()
        main(int(minutes_to_wait))
    except KeyboardInterrupt:
        pass
