import time

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
white = (255,255,255)
blank = (0,0,0)
colors = [blue,yellow,cyan,red,green,white]


class LedStrip:
    def __init__(self, width, height, between):
        self.height = height
        self.width = width
        self.between = between
        self.totalpixels = self.height * self.width + self.between * (self.width - 1)

    def get_pixel_index(self, xp, yp):
        offset = self.height * (xp - 1) + self.between * (xp - 1)
        if (xp % 2) == 0:
            offset = offset + (self.height - yp + 1)
        else:
            offset = offset + yp
        return offset

    def total_pixels(self):
        return self.totalpixels




# strip = LedStrip(5, 10, 2)
# print(strip.total_pixels())
# print(strip.get_pixel_index(3, 1))

#
# Generic Testing code
#

N = 15
M = 5
X = 5
#
totalpixels = N * X + M * (X -1 )
#
def get_pixel_index(xp, yp):
    offset = 0
    offset = N * (xp-1) + M * (xp-1)
    if (xp % 2)!=0:
        offset = offset + (N-yp+1)
    else:
        offset = offset + yp
    return offset

cnt = totalpixels

import ws2812b

pixels = ws2812b.ws2812b(290,0,22)

#
#
# pixels.set_pixel(get_pixel_index(1,1)-1, 100, 0, 0)
# pixels.set_pixel(get_pixel_index(2,2)-1, 0, 100, 0)
# pixels.set_pixel(get_pixel_index(3,3)-1, 0, 0, 100)
#
pixels.brightness(75)
#
pixels.fill(0, 0, 0)
pixels.show()
#

for color in colors:
    for bt in range(25, 90, 10):
        pixels.brightness(bt)
        pixels.fill(color[0], color[1], color[2])
        pixels.show()
        time.sleep(0.2)

pixels.fill(0, 0, 0)
pixels.show()
#
#
