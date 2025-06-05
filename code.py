try:
    import board
except ModuleNotFoundError:
    pass
else:
    from src.drivers.slider_trinkey import make_slider_trinkey_devices
    from src.interact import run

    # Setup board
    potentiometer, touch, pixels = make_slider_trinkey_devices()
    print("Loaded Trinkey...")

    # Call our run function
    run(potentiometer, touch, pixels)
