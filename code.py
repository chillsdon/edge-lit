#https://learn.adafruit.com/circuitpython-led-animations/overview
import time
import board
import neopixel
import microcontroller
import digitalio
from adafruit_debouncer import Debouncer
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.solid import Solid
#from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, BLACK, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE

pixel_pin = board.D12
# The number of NeoPixels
num_pixels = 29
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

colourArray = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE]
colourArrayIndex = 0
pixelColour = colourArray[colourArrayIndex]

pin1 = digitalio.DigitalInOut(board.D10)
pin1.direction = digitalio.Direction.INPUT
pin1.pull = digitalio.Pull.UP
switch1 = Debouncer(pin1)

pin2 = digitalio.DigitalInOut(board.D7)
pin2.direction = digitalio.Direction.INPUT
pin2.pull = digitalio.Pull.UP
switch2 = Debouncer(pin2)

# Basic Animations
solid = Solid(pixels, color=pixelColour)
#colorcycle = ColorCycle(pixels, 0.5, colors=[MAGENTA, ORANGE, TEAL])
blink = Blink(pixels, speed=0.5, color=pixelColour)
comet = Comet(pixels, speed=0.02, color=pixelColour, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=pixelColour, period=3)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=pixelColour)

# Sparkle Animations
sparkle = Sparkle(pixels, speed=0.05, color=pixelColour, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=pixelColour)

# Rainbow Animations
rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.02, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)

# Full animation sequence - disable auto-advance so we can control it manually
animations = AnimationSequence(
    solid, blink, comet, pulse, chase, sparkle, sparkle_pulse,
    rainbow, rainbow_chase, rainbow_comet, rainbow_sparkle,
    auto_clear=True,
    advance_interval=None  # Disable auto-advance
)

while True:
    animations.animate()

    switch1.update()
    if switch1.fell:
        print("Button 1 pressed - switching animation")  # Debug output
        animations.next()

    switch2.update()
    if switch2.fell:
        print("Button 2 pressed - changing colour")  # Debug output
        colourArrayIndex += 1
        if colourArrayIndex > len(colourArray) - 1:
            colourArrayIndex = 0
        pixelColour = colourArray[colourArrayIndex]
        # Update each animation's colour (rainbow animations don't support colour changes)
        solid.color = pixelColour
        blink.color = pixelColour
        comet.color = pixelColour
        pulse.color = pixelColour
        chase.color = pixelColour
        sparkle.color = pixelColour
        sparkle_pulse.color = pixelColour
