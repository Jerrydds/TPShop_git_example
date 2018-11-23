import pytest
import time

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # def teardown(self):
    #     self.driver.quit()

    def test_address(self):
        self.page.home.click_mine()
        self.page.mine.click_setting()
        # 判断条件为flass，则执行if（未登录，则先登录）
        if not self.page.mine.is_login():
            self.page.mine.click_sign_up_and_login()
            self.page.sign_up_and_login.input_phone("18503080305")
            # 输入密码
            self.page.sign_up_and_login.input_password("123456")
            # 点击登录
            self.page.sign_up_and_login.click_login()

        self.page.mine.click_address()
