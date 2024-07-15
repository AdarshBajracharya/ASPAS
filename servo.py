import serial
import time
from pynput import keyboard

# Set up the serial connection
ser = serial.Serial('COM9', 9600)  # Replace 'COM9' with your port

def send_command(command):
    ser.write(command.encode())

def on_press(key):
    try:
        if key.char == 'a':
            send_command('a')
        elif key.char == 'd':
            send_command('d')
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

ser.close()