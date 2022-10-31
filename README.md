### Code to use a NeoPixel strip without cutting /rewiring to create an LED board


Main script is neomat_test.py

In below layout ....

```
in =>  X X X X X 00
    00 X X X X X 00
    00 X X X X X   

width = 5 
height = 3
between = 4
(so, the total strip length would be at-least = 
width * height + between * (height -1)

```

## Sample code
```
pin = 22
width = 3
height = 13
between = 6
color = [0, 0, 50]

mat = NeoMat_Text.Matrix(pin, width, height, between, color)

mat.scroll(".")

```

Also read [http://www.pibits.net/code/raspberry-pi-pico-and-neopixel-example-in-micropython.php](http://www.pibits.net/code/raspberry-pi-pico-and-neopixel-example-in-micropython.php)
From the Adafruit NeoPixels best practices guide:

Before connecting NeoPixels to any large power source (DC “wall wart” or even a large battery), add a capacitor (1000 µF, 6.3V or higher) across the + and – terminals.

Place a 300 to 500 Ohm resistor in series between the Arduino data output pin and the input to the first NeoPixel. This resistor must be at the NeoPixel end of the wire to be effective!

Try to minimize the distance between the Arduino and first pixel.

Avoid connecting NeoPixels to a live circuit. If you simply must, always connect ground first, then +5V, then data. Disconnect in the reverse order.

If powering the pixels with a separate supply, apply power to the pixels before applying power to the microcontroller.