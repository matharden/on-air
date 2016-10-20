from sense_hat import SenseHat
from time import sleep
import sys

message = sys.argv[1]

print("Showing no entry sign with message: %s" % message)

sense = SenseHat()

r = [255, 0, 0]
o = [255, 127, 0]
w = [255, 255, 255]
b = [0, 0, 0]

stop_sign = [
b,b,r,r,r,r,b,b,
b,r,r,r,r,r,r,b,
r,r,r,r,r,r,r,r,
r,w,w,w,w,w,w,r,
r,w,w,w,w,w,w,r,
r,r,r,r,r,r,r,r,
b,r,r,r,r,r,r,b,
b,b,r,r,r,r,b,b
]

angles = [0, 90, 0, 90, 0, 90, 0, 90, 0]

while True:
    sense.show_message(message, text_colour=[255, 0, 0])
    sense.set_pixels(stop_sign)
    for a in angles:
        sense.set_rotation(a)
        sleep(1)
    sense.clear()
