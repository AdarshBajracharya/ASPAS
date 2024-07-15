import serial
from pynput import keyboard

# Set up the serial connection
ser = serial.Serial('COM10', 9600)  # Replace 'COM9' with your port

def send_command(command):
    ser.write(command.encode())

def on_press(key):
    try:
        if key.char == 'w':
            send_command('w')
        elif key.char == 's':
            send_command('s')
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener
    # Send space character to stop motors when the key is released
    send_command(' ')

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

ser.close()
