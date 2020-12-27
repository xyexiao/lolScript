import win32api
import win32gui

while True:
    base_position = win32api.GetCursorPos()
    window_handle = win32gui.WindowFromPoint(win32api.GetCursorPos())
    if window_handle > 0:
        window_position = win32gui.GetWindowRect(window_handle)
        class_name = win32gui.GetClassName(window_handle)
        text_name = win32gui.GetWindowText(window_handle)
        position = (base_position[0] - window_position[0],
                    base_position[1] - window_position[1])
        print(f"\r{window_handle}:{position}", end="")
        # print(f"\r{window_handle}:{window_position}", end="")
        # print(f"\r{class_name},{text_name}", end="")
    else:
        print(f"\r{base_position}", end="")
