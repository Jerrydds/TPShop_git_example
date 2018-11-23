import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AddressListPage(BaseAction):
    new_address_button = By.XPATH, "//*[contains(@text,'新建地址')]"

    def click_new_address(self):
        self.click(self.new_address_button)
