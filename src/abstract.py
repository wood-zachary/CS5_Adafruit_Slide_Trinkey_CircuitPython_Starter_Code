"""Collection of abstract classes for type hinting in the rest of the project.

(For students: don't worry about the code that's in here.
These classes are just providing examples of how to use the sensors
and other peripherals for type hinting.
The actual implementations of the classes are on the device.)
"""
# We aren't using the abc module because it isn't available on circuitpy.

# When making a project, remove any abstract classes you aren't using. 
# The boards do not have enough memory to handle dozens of abstract classes.

class LEDController:
    """Abstract LED controller."""

    def fill(self, color: tuple[int, int, int]) -> None:
        """Change the color of the LED being controlled.

        Args:
            color: Three-tuple of integers in [0, 255] representing the values
                of red, green, and blue to display on the LED.

        Example:
            `px.fill((0, 0, 0))` turns the LED off
        """
        raise NotImplementedError


class TouchSensor:
    """Abstract touch sensor."""

    @property
    def value(self) -> bool:
        """If the sensor is being touched.

        Example:
            `touch.value`
        """
        raise NotImplementedError

class AnalogSlider:
    """Abstract slide potentiometer (e.g., NeoSlider or Slider Trinkey).

    Provides raw ADC readings and converted voltage.

    Example:
        # Suppose `slider` is an instance of a concrete AnalogSlider driver:
        raw_value = slider.raw           # e.g., 0–65535
        volts = slider.voltage           # e.g., 0.0–3.3
        print(f"Raw: {raw_value}, Voltage: {volts:.2f} V")
    """

    @property
    def raw(self) -> int:
        """Raw ADC reading from the slider.

        Returns:
            Integer ADC value (e.g., 0–65535 or 0–4095, depending on hardware).

        Example:
            raw = slider.raw
        """
        raise NotImplementedError

    @property
    def voltage(self) -> float:
        """Converted voltage corresponding to the raw ADC value.

        Returns:
            Float voltage (e.g., 0.0–3.3 V).

        Example:
            volts = slider.voltage
        """
        raise NotImplementedError
