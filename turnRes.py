#imports

import pystray
import pywintypes
import win32api
import win32con
import ctypes
from PIL import Image
from pystray import MenuItem as item

from screeninfo import get_monitors

def get_size_zero():
    monitors = get_monitors()
    if monitors:
        monitor = monitors[0]
        return monitor.width, monitor.height
    return None, None


def on_set_resolution(width: int, height: int):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)

def on_quit():
    icon.visible = False
    icon.stop()


def resActual():
    user32=ctypes.windll.user32

    widthA = user32.GetSystemMetrics(0)
    heightA = user32.GetSystemMetrics(1)

    return widthA, heightA


if __name__ == "__main__":

    widthA,heightA = resActual()

    widthP, heightP = get_size_zero()

    image = Image.open("expandir.png")

    menu = (
        item(f"{widthP} Padrão", lambda:on_set_resolution(widthP,heightP)),
        item("-------------------", lambda:""),


        item("3200x1800", lambda:on_set_resolution(3200,1800)),
        item("-------------------", lambda:""),

        item(f"Atual: {widthA}x{heightA}",lambda:""),
        item("Sair", on_quit)
    )


    icon=pystray.Icon("Resolution Switcher", image,"Resolution Switcher", menu)
    icon.run()