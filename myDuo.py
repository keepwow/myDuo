from datetime import datetime
import os
import subprocess
from pynput import keyboard

def captureDuo():
    current_time = datetime.now()
    dirPath = os.environ['HOME'] + '/Pictures/Duolingo/'
    datePath = current_time.strftime("%Y-%m-%d")
    dirName = dirPath + datePath
    fileName = current_time.strftime("%H-%M-%S-%f")
    fileType = '.png'

    # Check if the directory exists
    if not os.path.exists(dirName):
        # Create the directory
        os.mkdir(dirName)

    savedFile = dirName + '/' + fileName + fileType

    # Take screencapture
    print('---' * 3, 'Capturing...' , fileName, '---' * 3)
    subprocess.check_output(['screencapture', savedFile], universal_newlines=True)

# https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))
    if f'{key}' == 'Key.enter':
        captureDuo()

def on_release(key):
    # print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()
