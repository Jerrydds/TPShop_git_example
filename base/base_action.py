from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def click(self, feature):
        self.find_element(feature).click()

    # 定位 toast元素,并返回文本内容
    def find_toast(self, key_word):
        feature = By.XPATH, "//*[contains(@text,'" + key_word + "')]"
        return self.find_element(feature, timeout=5, poll=0.1).text

    # 定义查找 toast 的返回状态
    def is_toast_exits(self, key_word):
        try:
            self.find_toast(key_word)
            return True
        except Exception:
            return False
        # 想知道toast 是否定位到,也可以这样写
        # try:
        #     feature = By.XPATH, "//*[contains(@text,'" + key_word + "')]"
        #     self.find_element(feature, timeout=5, poll=0.1)
        #     return True
        # except Exception:
        #     return False

    # 定义元素状态是否可用,某属性来决定
    def is_feature_enabled(self, feature):

        return self.find_element(feature).get_attribute("enabled") == "true"
        # <==>
        # 定义查找 toast 的返回状态
        # if self.find_element(feature).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False

    # 定位 元素并返回状态
    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False
