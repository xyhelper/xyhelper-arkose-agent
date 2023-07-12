import time
import undetected_chromedriver as uc
import logging

# 创建日志记录器
logging.basicConfig(filename='screenshot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# 创建浏览器实例
driver = uc.Chrome(headless=True, use_subprocess=False)
driver.get('https://chatarkose.xyhelper.cn')

while True:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    # screenshot_path = f'/data/nowsecure_{timestamp}.png'
    screenshot_path = f'/data/nowsecure.png'


    driver.save_screenshot(screenshot_path)
    print(f'Screenshot captured at {timestamp}')

    time.sleep(5)  # 等待5秒
