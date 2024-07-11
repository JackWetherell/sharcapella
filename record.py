import time
from pynput import keyboard

# Initialize an empty list to store the array elements
array = []

# Flag to indicate if the space key is pressed
space_pressed = False

# Function to handle key press events
def on_press(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True

# Function to handle key release events
def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = False
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Press 'Esc' to stop.")

try:
    while True:
        if space_pressed:
            array.append(80.0)
            print(1)
        else:
            array.append(150.0)
            print(0)
        
        # Wait for 0.01 seconds
        time.sleep(0.1)
        
        # Exit loop if listener has stopped
        if not listener.running:
            break

except KeyboardInterrupt:
    pass

print("Final array:", array)


import numpy as np
from scipy.ndimage import gaussian_filter1d


# Define the sigma for the Gaussian filter
sigma = 1.0

# Apply the Gaussian filter to smooth the array
smoothed_array = gaussian_filter1d(array, sigma)

print("Original array:", array)
print("Smoothed array:", smoothed_array)

import matplotlib.pyplot as plt

plt.plot(array)
plt.plot(smoothed_array)
plt.show()

def format_for_arduino(arr):
    formatted_array = ", ".join(f"{int(x)}" for x in arr)
    return f"int chan[] = {{{formatted_array}}};"

print(format_for_arduino(smoothed_array))