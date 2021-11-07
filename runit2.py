# import ws2812b

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


# N = 10
# M = 2
# X = 5
#
# totalpixels = N * X + M * (X -1 )
#
# def get_pixel_index(xp, yp):
#     offset = 0
#     offset = N * (xp-1) + M * (xp-1)
#     if (xp % 2)==0:
#         offset = offset + (N-yp+1)
#     else:
#         offset = offset + yp
#     return offset

strip = LedStrip(5, 10, 2)
print(strip.total_pixels())
print(strip.get_pixel_index(3, 1))

# cnt = totalpixels

# pixels = ws2812b.ws2812b(cnt,0,22)
#
#
# # pixels.set_pixel(get_pixel_index(1,1)-1, 100, 0, 0)
# # pixels.set_pixel(get_pixel_index(2,2)-1, 0, 100, 0)
# # pixels.set_pixel(get_pixel_index(3,3)-1, 0, 0, 100)
#
# pixels.brightness(75)
#
# for x in range(1,X+1):
#     for y in range(1, N+1):
#         pixels.set_pixel( get_pixel_index(x,y)-1, 0, 50, 50)
#
#
# pixels.show()
