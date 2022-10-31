import NeoMat_Text


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
white = (255,255,255)
blank = (0,0,0)
colors = [blue,yellow,cyan,red,green,white]

#
# https://www.digikey.in/en/maker/projects/raspberry-pi-pico-and-rp2040-micropython-part-3-pio/3079f9f9522743d09bb65997642e0831
#               https://makersportal.com/blog/ws2812-ring-light-with-raspberry-pi-pico
#  GOD BLOG : https://iris.artins.org/electronics/glitchy-neopixels/
#
pin = 22
width = 16
height = 10
between = 6
color = [0, 0, 50]

mat = NeoMat_Text.Matrix(pin, width, height, between, color)

mat.scroll("!")
