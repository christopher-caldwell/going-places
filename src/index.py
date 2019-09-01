#!/usr/bin/env python

"""
Displaying commute time
"""
from config.demo_opts import get_device
from config.config import minutes_between_commute_refresh
from get_commute_time import write_to_screen


def main(minutes_to_wait, device):
    write_to_screen(minutes_to_wait, device)


if __name__ == "__main__":
    try:
        device = get_device()
        main(minutes_between_commute_refresh, device)
    except KeyboardInterrupt:
        pass
