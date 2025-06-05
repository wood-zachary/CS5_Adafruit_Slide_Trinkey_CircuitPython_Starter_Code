from .abstract import AnalogSlider, TouchSensor, LEDController
# from .pulse import run_simple_pulse
# from .pot_pulse import run_pot_pulse
from .macros import run_macros

'''
Always comment out any imports you're not using to save memory.
'''

def run(potentiometer: AnalogSlider, touch: TouchSensor, pixels: LEDController):
    """
    Runs the selected demo on the Trinkey.

    Args:
        potentiometer: AnalogSlider
        touch: TouchSensor
        pixels: LEDController
    """
    # run_simple_pulse(pixels)
    # run_pot_pulse(potentiometer, pixels)
    run_macros(potentiometer, pixels)
