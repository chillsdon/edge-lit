# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import microcontroller
import digitalio
from adafruit_debouncer import Debouncer
from adafruit_led_animation.sequence import AnimationSequence

from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.chase import Chase

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse

from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle

from adafruit_led_animation.color import RED, YELLOW, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, BLACK, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D12

# The number of NeoPixels
num_pixels = 72

mode = 1
maxMode = 4

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

#pixelColour = AMBER

pin = digitalio.DigitalInOut(board.D10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
switch = Debouncer(pin)

#Basic Animations
colorcycle = ColorCycle(pixels, 0.5, colors=[MAGENTA, ORANGE, TEAL])
blink = Blink(pixels, speed=0.5, color=ORANGE)
comet = Comet(pixels, speed=0.02, color=MAGENTA, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)

#Sparkle Animations
sparkle = Sparkle(pixels, speed=0.05, color=TEAL, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=JADE)

#Rainbow Animations
rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)

#animations = AnimationSequence(
#    blink, comet, chase, sparkle, advance_interval=5, auto_clear=True
#)

animations = AnimationSequence(
    colorcycle, blink, comet, pulse, chase, sparkle, sparkle_pulse, rainbow, rainbow_chase, rainbow_comet, rainbow_sparkle, auto_clear=True
)

display = chase

while True:
    #display.animate()
    animations.animate()

    switch.update()

    if switch.fell:
        animations.next()        

        #mode += 1

        #if mode > maxMode:
        #    mode = 1

        #if mode == 1:
        #    display.color = AMBER

        #if mode == 2:
        #    display.color = MAGENTA

        #if mode == 3:
        #    display.color = TEAL

        #if mode == 4:
        #    display.color = JADE