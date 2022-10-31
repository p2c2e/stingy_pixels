import ws2812b
import time


cnt = 290 # 45
pixels = ws2812b.ws2812b(cnt,0,22)

pixels.fill(0, 0, 0)    
pixels.show() 