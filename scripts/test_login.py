from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_data("test_login"))
    def test_login(self):

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_login_signup()
