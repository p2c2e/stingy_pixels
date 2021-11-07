# led array
# N pixels tall, M pixels in twist, X pixels in wide

N = 10
M = 2
X = 3

totalpixels = N * X + M * (X -1 )

def get_pixel_index(xp, yp):
    offset = 0
    offset = N * (xp-1) + M * (xp-1)
    if (xp % 2)==0:
        offset = offset + (N-yp+1)
    else:
        offset = offset + yp
    return offset


print(get_pixel_index(1, 1))