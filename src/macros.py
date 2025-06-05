from .abstract import LEDController, AnalogSlider 
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode 
# from adafruit_hid.consumer_control import ConsumerControl
# from adafruit_hid.consumer_control_code import ConsumerControlCode 
# from adafruit_hid.mouse import Mouse
from support.mytyping import NoReturn

def run_macros(potentiometer: AnalogSlider, pixels: LEDController) -> NoReturn:
    THRESHOLD = 65535 * 2 // 3
    DURATION = 0.25
    INTERVAL = 0.05
    GREEN = ((0, 150, 0))
    YELLOW = ((75, 75, 0))

    kb_macro = Keycode.SPACE
    kb = Keyboard(usb_hid.devices) 
    # cc = ConsumerControl(usb_hid.devices)
    # ms = Mouse(usb_hid.devices)
    pixels.fill(YELLOW)
    
    last_raw_adc = 0
    
    while True:
        raw_adc = potentiometer.raw

        if raw_adc > THRESHOLD and last_raw_adc <= THRESHOLD:
            ...
            ### Your Code Here!
        
        last_raw_adc = raw_adc

        time.sleep(INTERVAL)


