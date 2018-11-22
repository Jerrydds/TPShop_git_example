import random

import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name


# 定义循环8次,生成0~9随机数
def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
        return password

# 定义循环2次,生成8位随机数拼接到列表中
def password_list():
    passwords = list()
    for i in range(2):
        passwords.append(random_password())
    return passwords


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login"))
    # def test_login(self, args):
    #     phone = args["phone"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_sign_up_and_login()
    #     # 输入用户名
    #     self.page.sign_up_and_login.input_phone(phone)
    #     # 输入密码
    #     self.page.sign_up_and_login.input_password(password)
    #     # 点击登录
    #     self.page.sign_up_and_login.click_login()
    #     # 判断toast是否存在
    #     # if self.page.sign_up_and_login.is_toast_exits(expect):
    #     #     return True
    #     # else:
    #     #     return False
    #     # <==>
    #     assert self.page.sign_up_and_login.is_toast_exits(expect)

    # # 只输入用户名或密码的脚本
    # @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     phone = args["phone"]
    #     password = args["password"]
    #
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_sign_up_and_login()
    #     # 输入用户名
    #     self.page.sign_up_and_login.input_phone(phone)
    #     # 输入密码
    #     self.page.sign_up_and_login.input_password(password)
    #
    #     # 这样写是判断,按钮置灰,才算通过
    #     assert not self.page.sign_up_and_login.is_login_button_enabled()
    #     # <==>
    #     # # 判断登录按钮的状态
    #     # if self.page.sign_up_and_login.is_login_button_enabled() == False:
    #     #     assert True
    #     # else:
    #     #     assert False

    # 显示密码,可等同toast那样处理,text由用户定义,然后匹配查找
    @pytest.mark.parametrize("password", password_list())
    def test_show_password(self, password):
        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_sign_up_and_login()
        # 输入用户名  -- 以下 if 为判断所有元素text为password.text,所以不用例外定义元素去模拟输入和密码一样的内容
        # self.page.sign_up_and_login.input_phone("123")
        # 输入密码
        self.page.sign_up_and_login.input_password(password)

        if self.page.sign_up_and_login.is_show_password_text_exist(password):
            assert False

        self.page.sign_up_and_login.click_show_password()
        # 如果找到输入的密码，那么断言为true
        assert self.page.sign_up_and_login.is_show_password_text_exist(password)
