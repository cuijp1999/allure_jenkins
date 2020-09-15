import allure
from selenium import webdriver


class Test_001:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test_01(self):
        print('\n test_001')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('第二步')
    def test_02(self):
        print('\n test_002')
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('第三步')
    def test_03(self):
        print('\n test_003')

    @allure.severity(allure.severity_level.MINOR)
    @allure.step('第四步')
    def test_04(self):
        print('\n test_004')

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step('第五步')
    def test_05(self):
        print('\n test_005')
