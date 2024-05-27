# -*- coding: UTF-8 -*-
import time
import logging

from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.confRead import Config

config_instance = Config()
platformName = config_instance.read_android_se()["platformName"]
platformVersion = config_instance.read_android_se()["platformVersion"]
deviceName = config_instance.read_android_se()["deviceName"]
logging.info(deviceName)
appPackage = config_instance.read_android_se()["appPackage"]
appActivity = config_instance.read_android_se()["appActivity"]
noReset = config_instance.read_android_se()["noReset"]


class DriverUtil:
    """Driver Utility类，用于管理App驱动程序的实例"""
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        """获取App端WebDriver实例。

        使用Appium通过指定的desired capabilities启动或返回现有的Appium WebDriver实例。
        """
        logging.info("尝试获取App端WebDriver...")

        desired_capabilities = {
            "platformName": platformName,  # 平台名称
            "platformVersion": platformVersion,  # Android系统版本
            "deviceName": deviceName,  # 设备或模拟器标识
            "appPackage": appPackage,  # 应用包名
            "appActivity": appActivity,  # 启动Activity
            "noReset": bool(noReset)
        }
        options = UiAutomator2Options().load_capabilities(desired_capabilities)
        appium_server_url = 'http://127.0.0.1:4723/wd/hub'
        if cls.__app_driver is None:
            try:
                cls.__app_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
                logging.info("Appium WebDriver初始化成功")
                time.sleep(3)  # 等待App加载
            except Exception as e:
                logging.error(f"初始化Appium WebDriver时发生错误: {e}")
                raise
        else:
            logging.info("复用已存在的Appium WebDriver实例")
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出并清理App端WebDriver实例。

        如果Appium WebDriver实例存在，则关闭它并重置类变量。
        """
        if cls.__app_driver is not None:
            logging.info("开始退出Appium WebDriver...")
            try:
                cls.__app_driver.quit()
                logging.info("Appium WebDriver已成功退出")
            except Exception as e:
                logging.error(f"退出Appium WebDriver时发生错误: {e}")
            finally:
                cls.__app_driver = None
                logging.info("Appium WebDriver实例已清空")
        else:
            logging.info("没有活动的Appium WebDriver实例需要退出")
