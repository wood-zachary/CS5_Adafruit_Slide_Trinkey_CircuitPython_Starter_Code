# src/drivers/slider_trinkey.py

import board
import analogio
import digitalio
import neopixel
from src.abstract import AnalogSlider, TouchSensor, LEDController

class _SliderPot(AnalogSlider):
    """
    Concrete driver for Adafruit Slider Trinkey (USB NeoPixel Slide Potentiometer).
    Uses board.POTENTIOMETER (16‑bit) and board.TOUCH, plus two NeoPixels.
    """
    def __init__(self):
        self._pot = analogio.AnalogIn(board.POTENTIOMETER)

    @property
    def raw(self) -> int:
        """Raw 16‑bit ADC reading (0–65535)."""
        return self._pot.value

    @property
    def voltage(self) -> float:
        """Convert raw ADC to voltage (0–3.3 V)."""
        return (self._pot.value * 3.3) / 65535.0

class _SliderTouch(TouchSensor):
    """Wraps the capacitive TOUCH pad on the Slider Trinkey."""
    def __init__(self):
        self._touch = digitalio.DigitalInOut(board.TOUCH)
        self._touch.direction = digitalio.Direction.INPUT

    @property
    def value(self) -> bool:
        return self._touch.value

class _SliderPixels(LEDController):
    """Wraps the two onboard NeoPixels."""
    def __init__(self, brightness: float = 0.1):
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=brightness)

    def fill(self, color: tuple[int, int, int]) -> None:
        self._pixels.fill(color)

def make_slider_trinkey_devices():
    """
    Returns (AnalogSlider, TouchSensor, LEDController) for Slider Trinkey.
    Usage:
        pot, touch, pixels = make_slider_trinkey_devices()
        print(pot.raw, pot.voltage, touch.value)
        pixels.fill((255,0,0))
    """
    pot = _SliderPot()
    touch = _SliderTouch()
    pixels = _SliderPixels()
    return pot, touch, pixels
