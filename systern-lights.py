#!/usr/bin/env python

from __future__ import print_function 
import time
import random
import unicornhat


print("""
Systerns super duper awesome unicorn lighting
""")

unicornhat.set_layout(unicornhat.AUTO)
unicornhat.rotation(0)
unicornhat.brightness(1)


GRID_WIDTH, GRID_HEIGHT = unicornhat.get_shape()
TRANSITION_SLEEP_TIMEOUT = 0.04  # change each pixel at this speed
CHANGE_COLOR_TIMEOUT = 5  # change color every 5 seconds


def get_rgb_val():
    # an RGB value is between 0 and 255
    return random.randint(0, 255)


def main():
    # grab 3 random values for RGB (note google: "RGB color codes")
    red   = get_rgb_val()
    green = get_rgb_val()
    blue  = get_rgb_val()
    print('%s, %s, %s' % (red, green, blue))

    for y in range(GRID_HEIGHT):
      for x in range(GRID_WIDTH):

        unicornhat.set_pixel(x, y, red , green, blue)
        unicornhat.show()

        time.sleep(TRANSITION_SLEEP_TIMEOUT)


if __name__ == "__main__":
    print('color timeout: %ss' % CHANGE_COLOR_TIMEOUT)
    while True:
        main()
        time.sleep(CHANGE_COLOR_TIMEOUT)




//we need to implement timeout code (turn on at 9 am turn off at 5 pm)
// maybe turn on at random times at the witching hour to freak anyone out here whos working late)


