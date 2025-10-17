from AutomationTool import AutomationTool
import configparser
import time
import sys
import argparse

trinity_cfg = '/home/chiu/python-test/trinity_test.cfg'
config = configparser.ConfigParser()
config.read(trinity_cfg, encoding='utf-8')

automatic = AutomationTool()

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

# box_led_r = wait_for_image(LED_R_IMG,3,10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Moniter LED test')
    parser.add_argument('LED_Type', help='LED_STARTED,LED_R,LED_G,LED_B')
    args = parser.parse_args()

    print(f"arg1 = {args.LED_Type}")
    led_type = args.LED_Type
    box = None

    if led_type == "LED_STARTED":
        box = wait_for_image(READ_TO_TEST_LED_IMG,2,20)
    elif led_type == "LED_R":
        box = wait_for_image(LED_R_IMG,3,10)
    elif led_type == "LED_G":
        box = wait_for_image(LED_G_IMG,3,10)
    elif led_type == "LED_B":
        box = wait_for_image(LED_B_IMG,3,10)
    


    if box != None:
        print("PASS")
        automatic.MouseClick(box.left,box.top)
    else:
        print("NG")
