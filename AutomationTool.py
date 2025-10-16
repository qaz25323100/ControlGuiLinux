import pyautogui
import time

class AutomationTool:

    def __init__(self):
        pass

    def KeyIn(self,Text='',interval = 0.05):
        pyautogui.typewrite(Text, interval=interval)

    def MouseClick(self,X,Y):
        pyautogui.click(X,Y)        
    
    def LocateImg(self,ImgPath='',TimeForNextAction=0.5):
        try:
            pyautogui.screenshot()
            time.sleep(TimeForNextAction)
            return pyautogui.locateOnScreen(ImgPath)
        except:
            return None        