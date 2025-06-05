# import time

from .pulse import pulse
from .abstract import LEDController, AnalogSlider
from support.mytyping import NoReturn

THRESHOLD: int = 65535 // 2

RED: tuple[int, int, int] = (150, 10, 10)
GREEN: tuple[int, int, int] = (30, 100, 10)


def pot_pulse(px: LEDController, color: tuple[int, int, int], raw_adc: int) -> None:
    """
    Maps potentiometer value to pulse duration and calls pulse.

    Args:
        px: LED controller object.
        color (tuple): color to pulse.
        prox (int): proximity value.
    """
    duration_ms = (raw_adc - THRESHOLD) * (50 - 1000) / (255 - THRESHOLD) + 1000
    pulse(px, color, duration_ms / 1000)


def run_pot_pulse(potentiometer: AnalogSlider, pixels: LEDController) -> NoReturn:
    """
    Runs potentiometer-based pulsing demo.

    Args:
        potentiometer: a potentiometer.
        pixels: LED controller object.
    """
    # Main loop
    while True:
        if potentiometer.raw >= THRESHOLD:
            # pulse(pixels, RED, 0.3)
            pot_pulse(pixels, RED, potentiometer.raw)
        else: 
            # pulse(pixels, GREEN, 0.3)
            pot_pulse(pixels, GREEN, potentiometer.raw)
