import ws2812b
import time


cnt = 290 # 45
pixels = ws2812b.ws2812b(cnt,0,22)

# pixels.set_pixel(5,10,0,0)
# pixels.set_pixel(1,0,0,20)
#  pixels.set_pixel_line(0, cnt-1, 0, 0, 0)

# pixels.set_pixel_line(0,cnt-1,0,20,0)
# for x in range(0, cnt):
#     pixels.set_pixel(x, 0,0, 20)
#     
# time.sleep(1)

for r in range(0, 255, 30):
    for g in range(0, 255, 30):
        for b in range(0, 255, 30):
            pixels.fill(r, g, b)
            pixels.show()
            time.sleep(1)
#     if(x%2 == 0):
#         pixels.fill(x, x, x)
#     else:
#         pixels.fill(0, 0, 0)
#         print("Zero")
#     pixels.show()
#     print(x, " Done")
#     time.sleep(1)
pixels.fill(0, 0, 0)    
# pixels.fill(0, 50, 0)
pixels.show() 