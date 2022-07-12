from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.baseLog import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 获取可视元素
    def get_visible_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            logger.error("获取元素失败：{}".format(e))
            logger.error('获取元素失败:"%s%s"' % locator)

    # 判断toast是否存在
    def is_toast_exist(self, text, timeout=3, poll_frequency=0.5):
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text, '%s')]" % text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(toast_loc)
            )
            return True
        except:
            return False
            # ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
            #     EC.presence_of_element_located(toast_loc)
            # )
        #     return ele.text
        # except:
        #     logger.error('未找到指定toast:"%s"' % toast_loc[1])

    def get_element_clickable(self, locator):
        """通过元素id获取该元素的enabled属性值，为false置灰不可点击，为true亮起可点击"""
        clickable = self.get_visible_element(locator).is_enabled()
        return clickable

    # 输入
    def input_action(self, loc, txt):
        self.get_visible_element(loc).send_keys(txt)

    # 点击
    def click_action(self, loc):
        self.get_visible_element(loc).click()

    # 清除
    def clear_action(self, loc):
        self.get_visible_element(loc).clear()

    # 关闭
    def quit_action(self):
        self.driver.close_app()
