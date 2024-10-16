import ctypes
import winsound
import os
import time
from datetime import datetime

# Function to play a sound
def play_alert_sound():
    winsound.Beep(1000, 500) 

# Function to get the current desktop background
def get_desktop_background():
    SPI_GETDESKWALLPAPER = 0x0073
    buffer = ctypes.create_unicode_buffer(500)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 500, buffer, 0)
    return buffer.value

# Function to set the background
def set_desktop_background(path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

# Function to log the change time
def log_change_time():
    with open("background_change_log.txt", "a") as log_file:
        print(f"Background changed at {datetime.now()}")
        log_file.write(f"Background changed at {datetime.now()}\n")

# Function to open a rickroll video
def open_rick_astley_video():
    video_path = "C:\\Users\\Sam\\Videos\\Rick.mp4" 
    os.startfile(video_path)

# Main function to monitor background changes
def monitor_background(interval=10):
    original_background = get_desktop_background()
    last_background = original_background

    while True:
        time.sleep(interval)
        current_background = get_desktop_background()

        if current_background != last_background:
            print(f"Background changed from {last_background} to {current_background}")
            open_rick_astley_video()
            # play_alert_sound()
            set_desktop_background(original_background)
            log_change_time()
            last_background = original_background

# Start monitoring with a 10-second interval
if __name__ == "__main__":
    monitor_background(interval=2) 