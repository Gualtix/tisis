import win32gui
import win32api

def draw_frame(x, y, width, height):
    dc = win32gui.GetDC(0)
    green = win32api.RGB(124,252,0)

    win32gui.SetPixel(dc, x, y, green)  # draw red at 0,0
    for i in range(x, x + width):

        win32gui.SetPixel(dc, i, y, green)
        win32gui.SetPixel(dc, i, y + height, green)

        win32gui.SetPixel(dc, i+1, y+1, green)
        win32gui.SetPixel(dc, i+1, y+1 + height, green)

    for i in range(y, y + height):

        win32gui.SetPixel(dc, x, i, green)
        win32gui.SetPixel(dc, x + width, i, green)

        win32gui.SetPixel(dc, x+1, i+1, green)
        win32gui.SetPixel(dc, x + width+1, i+1, green)
        
draw_frame(0, 0, 150, 150)

