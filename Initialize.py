import pyautogui
import subprocess
import time
import configparser
from AutomationTool import AutomationTool

import subprocess
import argparse

trinity_cfg = '/home/chiu/python-test/trinity_test.cfg'
# 創建 configparser 物件
config = configparser.ConfigParser()

# 讀取配置文件
config.read(trinity_cfg, encoding='utf-8')

# FWInputImg = config['App']['FWInputImg']
# Actionterval = float(config['App']['Actionterval'])
# KeyinInterval = float(config['App']['KeyinInterval'])
# ## \n for Enter
# FWPath = config['App']['FWPath'] + '\n'


def wait_for_image(image_path, interval=3, timeout=30):
    """
    每隔 interval 秒尋找一次 image_path 所指定的圖片，
    找到後回傳其位置 (Box)，否則在 timeout 秒後回傳 None。
    """
    start_time = time.time()
    
    while True:
        location = automatic.LocateImg(image_path)
        
        if location:
            print(f"Location：{location}")
            return location
        
        if time.time() - start_time > timeout:
            print("TIMEOUT!!Find the IMG ERROR!")
            return None
        
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initial Geotab GUI')
    # parser.add_argument('AppPath', help='AppPath')
    parser.add_argument('FWPath', help='FWPath')
    parser.add_argument('FWInputImg', help='FWInputImgPath')
    parser.add_argument('OP_ID', help='OP_ID')
    parser.add_argument('Actionterval', help='Actionterval')
    parser.add_argument('KeyinInterval', help='KeyinInterval')

    args = parser.parse_args()

    # AppPath = args.AppPath
    # AppName = AppPath.split("/")[-1]
    FWPath = args.FWPath
    FWInputImg = args.FWInputImg
    OP_ID = args.OP_ID
    Actionterval = float(args.Actionterval)
    KeyinInterval = float(args.KeyinInterval)

    time.sleep(2)
    # print("hello")
    automatic = AutomationTool()
    box = wait_for_image(FWInputImg,2,10)    
    automatic.MouseClick(box.left,box.top)
    time.sleep(Actionterval)
    automatic.KeyIn(FWPath,KeyinInterval)