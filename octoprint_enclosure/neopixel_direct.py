from rpi_ws281x import *
import sys
import time

LED_INVERT = False
LED_FREQ_HZ = 800000

if len(sys.argv) == 9:
    LED_PIN = int(sys.argv[1])
    LED_COUNT = int(sys.argv[2])
    LED_BRIGHTNESS = int(sys.argv[3])
    red = int(sys.argv[4])
    green = int(sys.argv[5])
    blue = int(sys.argv[6])
    LED_DMA = int(sys.argv[7])
    strip_type_name = sys.argv[8]
    strip_type = eval(strip_type_name)
else:
    print("fail")
    sys.exit(1)


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, freq_hz=LED_FREQ_HZ, dma=LED_DMA, invert=LED_INVERT, brightness=LED_BRIGHTNESS, strip_type=strip_type)
strip.begin()

color = Color(red, green, blue)

if strip_type_name.startswith('SK6812') and red == blue == green:
    color = Color(0,0,0,red)


for i in range(LED_COUNT):
    strip.setPixelColor(i, color)

strip.show()

print("ok")
