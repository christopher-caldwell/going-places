api_key = 'YOUR_GOOGLE_API_KEY_HERE'

# both can be coordinates, or just 123 Sesame Street
# since there are no spaces in coordinates, this is fine
origin = 'YOUR_ORIGIN_HERE'.replace(' ', '+')
destination = 'YOUR_DESTINATION_HERE'.replace(' ', '+')

# other options can be found here:
# https://developers.google.com/maps/documentation/directions/intro#VehicleType
mode = 'driving'

# Screen output color
color = 'yellow'

minutes_between_commute_refresh = 1

# 3 options for commutes are shown on the screen,
# 1 is current, 2 is if you'd leave in x minutes, and 3 is if you left in y minutes
option_2_minutes_offset = 20
option_3_minutes_offset = 60
