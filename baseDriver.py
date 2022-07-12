from appium import webdriver
from common.baseLog import logger

def android_driver():
    desired_caps = {
        "platformName": "android",
        # vivo
        # "platformVersion": "11",
        # "deviceName": "V2073A",
        # 华为
        "platformVersion": "10",
        "deviceName": "MXW_AN00",
        # oppo
        # "platformVersion": "11",
        # "deviceName": "PERM00",
        "appPackage": "com.atp.demo2",
        "appActivity": "com.atp.newarchitecture.activity.AppActivity",
        "autoGrantPermissions": "true",
        # 'unicodeKeyboard': True,  # 使用Unicode编码方式发送字符串
        'resetKeyboard': True  # 隐藏键盘
        # "resetKeyboard": "true",
    }
    # 启动app
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        logger.info("APP启动成功...")
        driver.implicitly_wait(5)
        return driver
    except Exception as e:
        logger.error("APP启动失败，原因是：{}".format(e))
        
#        testing


if __name__ == '__main__':
    android_driver()
