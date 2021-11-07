# import board as board
# import neopixel as neopixel
import ws2812b
import framebuf as framebuf
from math import ceil
import time

class Matrix:
    def __init__(self, pin, width, height, between, color):
        self.width = width
        self.height = height
        self.color = color
        self.between = between
        self.totalpixels = self.height * self.width + self.between * (self.width - 1)
        # pin = "board." + pin
        #this is a bad way to define the pin, but it works until a better way comes along
        #we are turing off the auto write to have smoother animation without the visible filling of pixles
#         self.pixels = neopixel.NeoPixel(pin, self.width * self.height, auto_write=False)
        self.pixels = ws2812b.ws2812b(self.totalpixels, 0, pin)
        self.buffer = bytearray(round(self.totalpixels / 8)) # self.width * self.height / 8))
        self.fb = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MVLSB)

    def get_pixel_index(self, xp, yp):
        
        offset = self.height * (xp - 1) + self.between * (xp - 1)
        if (xp % 2) == 0:
            offset = offset + (self.height - yp + 1)
        else:
            offset = offset + yp
        return offset

    def total_pixels(self):
        return self.totalpixels

    def neo_print_buffer(self, the_fb):
        #this simples goes through the frame buffer setting each pixel to either the color or off

        for y in range(self.height): # the_fb.height()):
            for x in range(self.width): # the_fb.width):
                if self.fb.pixel(x, y):
                    print(x,y, " => ", x+1, self.height - y, " = ", self.get_pixel_index(x+1, self.height-y), " of ", self.totalpixels)
                    self.pixels.set_pixel(self.get_pixel_index(x+1, self.height-y)-1, self.color[0], self.color[1], self.color[2])
                else:
                    self.pixels.set_pixel(self.get_pixel_index(x+1, self.height-y)-1, 0, 0, 0) #turn off unused


    def scroll(self, text):
        charBufSize = ceil(self.width/5)
        charWidth = 5
        #iterate through each letter taking a slice of letters just larger than the display and sliding them accross it
        for i in range(len(text)+1):
            cText = text[i:i+charBufSize]
            for j in range(charWidth+1):
                self.fb.fill(0)
                self.fb.text(cText, -1*(j), 0, True)
                #each time we refil the frame buffer with the text starting one place futher to the left so that
                #the text scrolls towards the left (hence the -1)
                self.neo_print_buffer(self.fb)
                self.pixels.show()
                time.sleep(1)
        else:
            #when finished turn all the LEDs off as sometimes the last column will be on
            self.fb.fill(0)
            self.neo_print_buffer(self.fb)
            self.pixels.show()
