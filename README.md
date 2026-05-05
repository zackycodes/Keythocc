# ⌨️ Keythocc: Mechanical Keyboard Sound Emulator
Transform your typing experience by triggering high-quality mechanical keyboard sounds with every keystroke. Whether you're using the Python implementation for simplicity or the Java version for performance, ThoccBoard brings the "thocc" to any setup.

## ✨ Features
* Multi-Language Support: Choose between Python and Java implementations.  
* Dynamic Sound Selection: Randomly assigns unique click sounds to different keys for a realistic, non-repetitive acoustic profile.  
* WPM Tracker: Built-in Words Per Minute (WPM) calculator accessible via hotkeys.  
* Low Latency: Utilizes multi-threading to ensure sounds play instantly without lagging your typing.  
* Anti-Repeat Logic: Prevents sound "stuttering" when holding down a key.  

## 🚀 Getting Started (Python)
Prerequisites
You will need the pynput and simpleaudio libraries.  

`Bash 
pip install pynput simpleaudio`

Usage
Ensure your .wav files are placed in the audio/ directory.
Run the script:

`Bash
python thocc.py`
Control:

* Esc: Exit the program.  
* Ctrl: Press once to start WPM measurement, press again to stop and see your result.  

## ⚙️ How it Works
The script monitors your hardware interrupts using a keyboard listener.
To ensure the typing experience remains fluid:
* Preloading: All audio files are loaded into memory as WaveObjects before the listener starts to minimize disk I/O delay.  
* Threading: Every sound is dispatched to a background thread, preventing the main listener from blocking.  
* Consistency: The script remembers which sound was assigned to which key during your session, mimicking the consistent sound of a specific physical switch.  

## 📝 Customization
To add or remove sounds, simply update the sound_files list in the source code:

```
Python
# thocc.py
sound_files = [
    'audio/custom_click_1.wav',
    'audio/custom_click_2.wav'
]
```
Happy typing! May your clicks be crisp and your thoccs be deep.
