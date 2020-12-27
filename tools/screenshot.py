import time
import os

import win32gui
from PIL import ImageGrab


game_name = "League of Legends (TM) Client"
client_name = "League of Legends"
save_dir = "images"
handle1 = win32gui.FindWindow(None, client_name)
if handle1:
    client_size = win32gui.GetWindowRect(handle1)
    if (client_size[2] - client_size[0]) != 1280 and \
            (client_size[3] - client_size[1]) != 720:
        hwndChildLIst = []
        win32gui.EnumChildWindows(
            handle1, lambda hwnd, param: param.append(hwnd), hwndChildLIst)
        for i in hwndChildLIst:
            s = win32gui.GetWindowRect(i)
            if (s[2] - s[0]) == 1280 and (s[3] - s[1]) == 720:
                handle1 = i
                break

handle2 = win32gui.FindWindow(None, game_name)
print(handle1, handle2)
handle = max(handle1, handle2)
window_position = win32gui.GetWindowRect(handle)
win32gui.SetForegroundWindow(handle)
time.sleep(1)
ImageGrab.grab(window_position).save(
    os.path.join(save_dir, str(int(time.time())) + ".png"))
