import pyautogui
import subprocess
import time
import configparser
from AutomationTool import AutomationTool

trinity_cfg = '/home/chiu/python-test/trinity_test.cfg'
config = configparser.ConfigParser()
automatic = AutomationTool()

# 讀取配置文件
config.read(trinity_cfg, encoding='utf-8')

Run_IMG = config['App']['Run_IMG']
DelayToLED = float(config['App']['DelayToLED'])
READ_TO_TEST_LED_IMG = config['LED']['READ_TO_TEST_LED_IMG']
LED_R_IMG = config['LED']['LED_R_IMG']
LED_G_IMG = config['LED']['LED_G_IMG']
LED_B_IMG = config['LED']['LED_B_IMG']

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

# Test Start
box_run = automatic.LocateImg(Run_IMG,0.5)
automatic.MouseClick(box_run.top,box_run.left)



# READ_TO_TEST_LED_IMG = wait_for_image(READ_TO_TEST_LED_IMG,3,30)

# box_led_r = wait_for_image(LED_R_IMG,3,20)
# print(box_led_r)
# box_led_g = wait_for_image(LED_G_IMG,1,20)
# box_led_b = wait_for_image(LED_B_IMG,1,20)