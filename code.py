# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import microcontroller
#import digitalio
#from adafruit_debouncer import Debouncer
#from adafruit_led_animation.sequence import AnimationSequence
#from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
#from adafruit_led_animation.animation.chase import Chase
#from adafruit_led_animation.animation.sparkle import Sparkle

#from adafruit_led_animation.color import RED
#from adafruit_led_animation.color import YELLOW
from adafruit_led_animation.color import ORANGE
#from adafruit_led_animation.color import GREEN
from adafruit_led_animation.color import TEAL
#from adafruit_led_animation.color import CYAN
#from adafruit_led_animation.color import BLUE
#from adafruit_led_animation.color import PURPLE
from adafruit_led_animation.color import MAGENTA
#from adafruit_led_animation.color import WHITE
#from adafruit_led_animation.color import BLACK
#from adafruit_led_animation.color import GOLD
#from adafruit_led_animation.color import PINK
#from adafruit_led_animation.color import AQUA
from adafruit_led_animation.color import JADE
#from adafruit_led_animation.color import AMBER
#from adafruit_led_animation.color import OLD_LACE

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D0

# The number of NeoPixels
num_pixels = 68

#mode = 1
#maxMode = 4

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

pixelColour = TEAL

#colourInt = random.randint(1, 4)

#if colourInt == 1:
#    pixelColour = ORANGE

#if colourInt == 2:
#    pixelColour = TEAL

#if colourInt == 3:
#    pixelColour = JADE

#if colourInt == 4:
#    pixelColour = MAGENTA

#pin = digitalio.DigitalInOut(board.D3)
#pin.direction = digitalio.Direction.INPUT
#pin.pull = digitalio.Pull.UP
#switch = Debouncer(pin)

#blink = Blink(pixels, speed=0.5, color=ORANGE)
comet = Comet(pixels, speed=0.01, color=pixelColour, tail_length=10, bounce=True)
#chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)
#sparkle = Sparkle(pixels, speed=0.05, color=pixelColour, num_sparkles=10)

#animations = AnimationSequence(
#    blink, comet, advance_interval=5, auto_clear=True, random_order=True
#)

while True:
    #switch.update()

    #if switch.fell:
    #    microcontroller.reset()

    #    mode = mode + 1

    #    if mode > maxMode:
    #        mode = 1

    #    if mode == 1:
    #        comet = Comet(pixels, speed=0.01, color=ORANGE, tail_length=10, bounce=True)

    #    if mode == 1:
    #        comet = Comet(pixels, speed=0.01, color=MAGENTA, tail_length=10, bounce=True)

    #    if mode == 1:
    #        comet = Comet(pixels, speed=0.01, color=AQUA, tail_length=10, bounce=True)

    #    if mode == 1:
    #        comet = Comet(pixels, speed=0.01, color=JADE, tail_length=10, bounce=True)

    comet.animate()