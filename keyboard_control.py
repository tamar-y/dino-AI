import keyboard
import time


def switch_window():
    keyboard.press_and_release('alt + tab')
    time.sleep(1)


def press_space():
    keyboard.press_and_release('space')
