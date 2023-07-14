import win32con
import win32api
import pywintypes


def set_resolution(width, height, refresh_rate=None):
    devmode = pywintypes.DEVMODEType()
    if refresh_rate is not None:
        print(f"Switching resolution to {width}x{height} at {refresh_rate}Hz")
        devmode.DisplayFrequency = refresh_rate
        devmode.Fields |= win32con.DM_DISPLAYFREQUENCY
    else:
        print("Switching resolution to {0}x{1}".format(width, height))
    devmode.PelsWidth = int(width)
    devmode.PelsHeight = int(height)
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    win32api.ChangeDisplaySettings(devmode, 0)
