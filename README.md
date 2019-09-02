# Going Places

Python script that shows commute times at various stages

This script is designed to be ran from a RaspberryPi, with a 256px L x 64px W screen

## Setup

Setup is designed to be as easy as possible. If anything could be easier, [let me know](https://github.com/caldwell619/going-places/issues)

### Keys

To get started, you'll need a Google Maps API key. Directions can be found [here](https://developers.google.com/maps/documentation/directions/get-api-key).

### Cloning

To clone the project for your use, run `git clone git@github.com:caldwell619/going-places.git`, in your intended directory

### Dependencies

To install the necessary dependencies, run `pip install -r requirements.txt`

## Config

Most of the configuration is confined to `config.py`. You'll need to create your own `config.py`, and fill in the appropriate values.

Follow the `example.config.py`

### api_key

This is your Google Maps Api Key

### origin

This is where you will be leaving from. It's a hard value, because this is designed to be used with a Pi, as a stationary display.

Can be coordinates, business name, or an address. Anything you would normally type into Google Maps.

### destination

Where you are going.

Can be coordinates, business name, or an address. Anything you would normally type into Google Maps.

### mode

This is the way you will be travelling. Available options can be found [here](https://developers.google.com/maps/documentation/directions/intro#VehicleType).

Default is `driving`

### color

The color of the output text

### minutes_between_commute_refresh

Number in minutes you'd like the script to wait before refreshing the commute time.

For example, 1 would refresh the commute every minute

### option_n_minutes_offset

This value repeats twice.

- The output on the **top** screen shows the time if you left now

- The output in the **middle** screen shows the time if you left in `option_2_minutes_offset`

- The output in the **bottom** screen shows the time if you left in `option_3_minutes_offset`

For example, `option_2_minutes_offset = 20` would have the middle screen option if you were leaving in **20 minutes**

## Running the script
