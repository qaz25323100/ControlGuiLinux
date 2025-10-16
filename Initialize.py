import pyautogui
import subprocess
import time
import configparser
from AutomationTool import AutomationTool

trinity_cfg = '/home/chiu/python-test/trinity_test.cfg'
# 創建 configparser 物件
config = configparser.ConfigParser()

# 讀取配置文件
config.read(trinity_cfg, encoding='utf-8')

FWInputImg = config['App']['FWInputImg']
Actionterval = float(config['App']['Actionterval'])
KeyinInterval = float(config['App']['KeyinInterval'])
## \n for New line
FWPath = config['App']['FWPath'] + '\n'

# Actionterval = float(config['App']['Actionterval'])
# KeyinInterval = float(config['App']['KeyinInterval'])
# try:
#     # Enter FW Path 
#     gedit = subprocess.Popen(["gedit"], stdin=subprocess.PIPE)
#     #gedit = subprocess.run(["gedit"], stdin=subprocess.PIPE)
#     time.sleep(1)
#     pyautogui.screenshot()
#     box = pyautogui.locateOnScreen('/home/chiu/python-test/find.png')
#     print(box)
#     pyautogui.click(box.left+box.width, box.top+box.height)
#     pyautogui.hotkey(['ctrl','space'])
#     time.sleep(0.5)
#     pyautogui.typewrite('https://stackoverflow.com/questions/73925578/pyautogui-was-unable-to-import-pyscreeze\n', interval=0.05)
# except Exception as e:
#     print(f"錯誤: {e}")
# finally:
#     print('管他有沒有錯，繼續啦！')
# Enter FW Path 
# gedit = subprocess.Popen(["gedit"], stdin=subprocess.PIPE)
#gedit = subprocess.run(["gedit"], stdin=subprocess.PIPE)


# time.sleep(Actionterval)
# pyautogui.screenshot()
# time.sleep(Actionterval)
# # pyautogui.screenshot('/home/chiu/python-test/foo.png')
# box = pyautogui.locateOnScreen(FWInputImg)
# print(box)
# time.sleep(Actionterval)

# pyautogui.click(box.left,box.top)
# # pyautogui.mouseDown()
# time.sleep(Actionterval) #or whatever you need, if even needed
# # pyautogui.mouseUp()
# # pyautogui.click(box.left, box.top+box.height)
# print(pyautogui.position())
# # pyautogui.click()

# # pyautogui.hotkey(['ctrl','space'])
# time.sleep(Actionterval)
# pyautogui.typewrite('https://stackoverflow.com/questions/73925578/pyautogui-was-unable-to-import-pyscreeze\n', interval=KeyinInterval)


    
automatic = AutomationTool()

# pyautogui.screenshot('/home/chiu/python-test/foo.png')
box = automatic.LocateImg(FWInputImg,0.5)
time.sleep(Actionterval)
automatic.MouseClick(box.left,box.top)
time.sleep(Actionterval)
automatic.KeyIn(FWPath,KeyinInterval)