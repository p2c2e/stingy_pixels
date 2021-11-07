import NeoMat_Text

pin = 22
width = 3
height = 13
between = 6
color = [0, 0, 50]

mat = NeoMat_Text.Matrix(pin, width, height, between, color)

mat.scroll(".")
