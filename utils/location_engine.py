import math

def adjust_price_by_location(price, lat, lon):

    center_lat = 42.6629
    center_lon = 21.1655

    distance = math.sqrt((lat - center_lat)**2 + (lon - center_lon)**2)

    if distance < 0.01:
        zone = "A"
        multiplier = 1.2
    elif distance < 0.02:
        zone = "B"
        multiplier = 1.0
    else:
        zone = "C"
        multiplier = 0.8

    new_price = price * multiplier
    diff = new_price - price


    return new_price, diff, zone, multiplier