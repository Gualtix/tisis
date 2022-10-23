import pyautogui

def mouseClick(x,y):
    #Resolution of the screen
    wh = pyautogui.size() 
    height = wh[1]
    width = wh[0]

    #Current position of the mouse
    current_x, current_y = pyautogui.position()
    print("Current position: " + str(current_x) + "," + str(current_y))

    #Move the mouse to the desired position
    pyautogui.moveTo(0,1078)
    #Click the mouse
    pyautogui.click()

def main():

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./screenshot.png')
    mouseClick(0,1080)


if __name__ == "__main__":
    main()


