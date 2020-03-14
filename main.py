from keyboard_control import *
from time import sleep

if __name__ == "__main__":
    switch_window()
    press_space()
    sleep(2)
    for _ in range(10):
        sleep(1)
        press_space()
