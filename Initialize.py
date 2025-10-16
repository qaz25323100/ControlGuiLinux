import pyautogui
import subprocess
import time
import configparser
from AutomationTool import AutomationTool

import subprocess

trinity_cfg = '/home/chiu/python-test/trinity_test.cfg'
# 創建 configparser 物件
config = configparser.ConfigParser()



# 讀取配置文件
config.read(trinity_cfg, encoding='utf-8')

AppPath = config['App']['AppPath']
AppName = AppPath.split("/")[-1]
FWInputImg = config['App']['FWInputImg']
Actionterval = float(config['App']['Actionterval'])
KeyinInterval = float(config['App']['KeyinInterval'])
## \n for Enter
FWPath = config['App']['FWPath'] + '\n'


# Kill by process name (Linux)

subprocess.run(["pkill", "-9", "-f",AppName])

# Start new process
# subprocess.Popen(["/usr/local/bin/python3.13",AppPath])
    
# print("hello")
# automatic = AutomationTool()

# box = automatic.LocateImg(FWInputImg,0.5)
# time.sleep(Actionterval)
# automatic.MouseClick(box.left,box.top)
# time.sleep(Actionterval)
# automatic.KeyIn(FWPath,KeyinInterval)