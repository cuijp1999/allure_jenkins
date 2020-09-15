import allure
from selenium import webdriver


class Test_001:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')

    @allure.step('第二步')
    def ooo(self):
        print('ooo')

    @allure.step('第一步')
    def test_01(self):
        self.ooo()
        # 添加截图          allure.attach(二进制参数, '截图名字', 图片类型)
        allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)
        print('\n ---test_001')
