import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login"))
    def test_login(self, args):
        phone = args["phone"]
        password = args["password"]
        expect = args["expect"]

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_sign_up_and_login()
        # 输入用户名
        self.page.sign_up_and_login.input_phone(phone)
        # 输入密码
        self.page.sign_up_and_login.input_password(password)
        # 点击登录
        self.page.sign_up_and_login.click_login()
        # 判断toast是否存在
        # if self.page.sign_up_and_login.is_toast_exits(expect):
        #     return True
        # else:
        #     return False
        # <==>
        assert self.page.sign_up_and_login.is_toast_exits(expect)

    # 只输入用户名或密码的脚本
    @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        phone = args["phone"]
        password = args["password"]

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_sign_up_and_login()
        # 输入用户名
        self.page.sign_up_and_login.input_phone(phone)
        # 输入密码
        self.page.sign_up_and_login.input_password(password)

        # 这样写是判断,按钮置灰,才算通过
        assert not self.page.sign_up_and_login.is_login_button_enabled()
        # <==>
        # # 判断登录按钮的状态
        # if self.page.sign_up_and_login.is_login_button_enabled() == False:
        #     assert True
        # else:
        #     assert False