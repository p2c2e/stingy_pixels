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
