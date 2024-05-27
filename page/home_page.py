# -*- coding: UTF-8 -*-
import logging
import os
import time

import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
from common.utils import DriverUtil


class DemoPage(BasePage):
    """对象库层"""

    def __init__(self):
        super().__init__()
        self.home_page = (By.XPATH, '//androidx.appcompat.app.ActionBar.c[@content-desc="首页"]')
        self.login = (By.ID, 'com.smile.gifmaker:id/left_text')
        self.mobile_login = (By.XPATH, '//android.widget.TextView[@text="手机号登录"]')
        self.mi_ma = (By.ID, 'com.smile.gifmaker:id/switch_login_way')
        # self.other_login = (By.ID, 'com.smile.gifmaker:id/btn_other_login_ways')
        self.user_agreement = (By.ID, 'com.smile.gifmaker:id/protocol_checkbox')
        self.account = (By.ID, 'com.smile.gifmaker:id/phone_et')
        self.user_password = (By.ID, 'com.smile.gifmaker:id/password_et')
        self.confirm_login = (By.ID, 'com.smile.gifmaker:id/confirm_btn')
        self.search = (By.ID, 'com.smile.gifmaker:id/search_btn')
        self.query_input = (By.ID, 'com.smile.gifmaker:id/editor')
        self.perform_search = (By.XPATH, '//android.widget.TextView[@text="搜索"]')
        self.select_user = (By.XPATH,
                            '//android.widget.HorizontalScrollView[@resource-id="com.smile.gifmaker:id/tabs"]/android.widget.LinearLayout/android.view.View[2]')

        self.i_home = (By.XPATH, '//androidx.appcompat.app.ActionBar.c[@content-desc="我"]')
        self.i_guan_zhu = (By.ID, 'com.smile.gifmaker:id/following_tv')
        self.i_zhi_bo = (By.XPATH, '//android.widget.TextView[@resource-id="com.smile.gifmaker:id/live_tip_text"]')

        self.z_srk = (By.ID, 'com.smile.gifmaker:id/live_comment_text_view')
        self.z_ssrr = (By.ID, 'com.smile.gifmaker:id/editor')
        self.z_fs = (By.ID, 'com.smile.gifmaker:id/finish_button')

    def find_home_page(self):
        return self.find_element(self.home_page)

    def find_login(self):
        return self.find_element(self.login)

    def find_mobile_login(self):
        return self.find_element(self.mobile_login)

    def find_other_login(self):
        return self.find_element(self.mi_ma)

    def find_user_agreement(self):
        return self.find_element(self.user_agreement)

    def find_account(self):
        return self.find_element(self.account)

    def find_password(self):
        return self.find_element(self.user_password)

    def find_confirm_login(self):
        return self.find_element(self.confirm_login)

    def find_search(self):
        return self.find_element(self.search)

    def find_query_input(self):
        return self.find_element(self.query_input)

    def find_perform_search(self):
        return self.find_element(self.perform_search)

    def find_select_user(self):
        return self.find_element(self.select_user)

    def find_i_home(self):
        return self.find_element(self.i_home)

    def find_i_guan_zhu(self):
        return self.find_element(self.i_guan_zhu)

    def find_i_zhi_bo(self):
        return self.find_element(self.i_zhi_bo)

    def find_z_srk(self):
        return self.find_element(self.z_srk)

    def find_z_ssrr(self):
        return self.find_element(self.z_ssrr)

    def find_z_fs(self):
        return self.find_element(self.z_fs)


class DemoHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.demo_page = DemoPage()

    def click_home_page(self):
        self.demo_page.find_home_page().click()

    def click_login(self):
        self.demo_page.find_login().click()

    def click_mobile_login(self):
        self.demo_page.find_mobile_login().click()

    def click_other_login(self):
        self.demo_page.find_other_login().click()

    def click_user_agreement(self):
        self.demo_page.find_user_agreement().click()

    def input_account(self, keyword):
        self.input(self.demo_page.find_account(), keyword)

    def input_user_password(self, keyword):
        self.input(self.demo_page.find_password(), keyword)

    def click_confirm_login(self):
        self.demo_page.find_confirm_login().click()

    def click_search(self):
        self.demo_page.find_search().click()

    def input_query_input(self, keyword):
        self.input(self.demo_page.find_query_input(), keyword)

    def click_select_user(self):
        self.demo_page.find_select_user().click()

    def click_perform_search(self):
        self.demo_page.find_perform_search().click()

    def click_i_home(self):
        self.demo_page.find_i_home().click()

    def click_i_guan_zhu(self):
        self.demo_page.find_i_guan_zhu().click()

    def click_i_zhi_bo(self):
        self.demo_page.find_i_zhi_bo().click()

    def click_z_srk(self):
        self.demo_page.find_z_srk().click()

    def input_z_ssrr(self, keyword):
        self.input(self.demo_page.find_z_ssrr(), keyword)

    def click_z_fs(self):
        self.demo_page.find_z_fs().click()


class DemoProxy:
    """业务层"""

    def __init__(self):
        self.demo_handler = DemoHandle()
        self.driver = DriverUtil.get_app_driver()

    def user_home_page(self):
        allure.attach(DriverUtil.get_app_driver().get_screenshot_as_png(), "精选页截图", allure.attachment_type.PNG)
        self.demo_handler.click_home_page()
        time.sleep(2)
        allure.attach(DriverUtil.get_app_driver().get_screenshot_as_png(), "首页截图", allure.attachment_type.PNG)

    def user_login(self):
        self.demo_handler.click_login()
        self.demo_handler.click_mobile_login()
        self.demo_handler.click_other_login()
        time.sleep(1)
        os.system('adb shell input keyevent 4')
        logging.info("adb 命令关闭输入法软键盘")
        self.demo_handler.input_account("13521520865")
        self.demo_handler.input_user_password("woshi123456")
        self.demo_handler.click_user_agreement()
        self.demo_handler.click_confirm_login()
        time.sleep(6)

    def select_user(self):
        self.demo_handler.click_search()
        time.sleep(3)
        os.system('adb shell input keyevent 4')
        logging.info("adb 命令关闭输入法软键盘")
        self.demo_handler.input_query_input("sxlfsska")
        self.demo_handler.click_perform_search()
        time.sleep(6)
        self.demo_handler.click_select_user()
        allure.attach(DriverUtil.get_app_driver().get_screenshot_as_png(), "用户截图", allure.attachment_type.PNG)
        time.sleep(6)
        self.driver.tap([(53, 465), (209, 621)], 1000)
        time.sleep(5)

    def i_home(self):
        self.demo_handler.click_i_home()
        logging.info("查找 我")
        self.demo_handler.click_i_guan_zhu()
        logging.info("点击 我的 关注")
        time.sleep(5)
        self.demo_handler.click_i_zhi_bo()
        logging.info("进入 直播间")
        time.sleep(10)

    def z_dan_mu(self, send_text):
        self.demo_handler.click_z_srk()
        self.demo_handler.input_z_ssrr(send_text)
        self.demo_handler.click_z_fs()
        time.sleep(10)
