from pynput import keyboard
import simpleaudio as sa
import random
import threading
import time

# List of your sound files (replace with your actual file paths)
sound_files = [
    'keyboard_click_1.wav',
    'keyboard_click_2.wav',
    'keyboard_click_3.wav',
    'keyboard_click_4.wav',
    'keyboard_click_5.wav'
#    'keyboard_click_8.wav'
    
]

# Preload all sound files into memory
wave_objects = [sa.WaveObject.from_wave_file(sound_file) for sound_file in sound_files]

# Dictionary to store the last sound played for each key
last_sound_played = {}
# Dictionary to track which keys are being held down
key_held = {}

# Variables for WPM calculation
typing_start_time = None
typed_chars = 0
wpm_calculation_active = False

def play_sound(wave_obj):
    """Function to play the sound in a separate thread."""
    wave_obj.play()

def on_press(key):
    global typing_start_time, typed_chars, wpm_calculation_active, key_held

    # If key is already held down, don't play the sound again
    if key in key_held and key_held[key]:
        return

    key_held[key] = True  # Mark the key as held down

    # Count characters typed
    if hasattr(key, 'char') and key.char is not None:
        typed_chars += 1

    try:
        # Get the character of the key pressed
        key_char = key.char
        print(key_char) #print(f'Key {key_char} pressed.')
    except AttributeError:
        # Handle special keys
        key_char = str(key)
        print(key) #print(f'Special key {key} pressed.')

    # Check if the sound for this key has already been played
    if key_char in last_sound_played:
        wave_obj = last_sound_played[key_char]  # Use the previously played sound
    else:
        # Randomly select a preloaded sound object
        wave_obj = random.choice(wave_objects)
        last_sound_played[key_char] = wave_obj  # Store it for future presses

    # Play the sound in a separate thread
    threading.Thread(target=play_sound, args=(wave_obj,)).start()

def calculate_wpm():
    global typing_start_time, typed_chars

    if typing_start_time is not None:
        elapsed_time = time.time() - typing_start_time
        wpm = (typed_chars / 5) / (elapsed_time / 60)  # WPM calculation
        
        typing_start_time = None
        typed_chars = 0

def on_release(key):
    global typing_start_time, wpm_calculation_active, key_held

    # Mark the key as released
    if key in key_held:
        key_held[key] = False

    if key == keyboard.Key.esc:
        # Stop listener
        return False

    # Check for Ctrl + `
    if key == keyboard.Key.ctrl and not wpm_calculation_active:
        # Start timing
        typing_start_time = time.time()
        wpm_calculation_active = True
        print("WPM measurement started. Start typing...")

    elif key == keyboard.Key.ctrl and wpm_calculation_active:
        # Calculate WPM when Ctrl is released
        calculate_wpm()
        wpm_calculation_active = False
        print("WPM measurement stopped.")

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
