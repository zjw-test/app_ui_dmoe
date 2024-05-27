# -*- coding: UTF-8 -*-
import logging
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from common.utils import DriverUtil


class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_app_driver()
        logging.info("Appium WebDriver 初始化成功")

    def find_element(self, loc, timeout=5, poll_frequency=0.5, max_retries=3):
        retry_count = 0
        while retry_count <= max_retries:
            try:
                element = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
                logging.info(f"找到元素: {loc}")
                return element
            except (NoSuchElementException, TimeoutException) as e:
                logging.warning(f"尝试查找元素: {loc} 失败, 第{retry_count + 1}次重试. 原因: {e}")
                retry_count += 1
                # 根据实际情况决定是否需要增加延迟或调整策略
                if retry_count < max_retries:
                    time.sleep(1)  # 简单示例，增加1秒延迟，实际中可按需调整
        logging.error(f"查找元素失败: {loc}，已达到最大重试次数.")

    def find_elements(self, loc, timeout=10, poll_frequency=0.5):
        try:
            elements = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
            if elements:
                logging.info(f"找到多个元素: {loc}")
            else:
                logging.info(f"在指定位置未找到任何元素: {loc}")
            return elements
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"查找多个元素失败: {loc}, 原因: {e}")


class BaseHandle:
    def input(self, el, info):
        logging.info(f"开始输入信息到元素: {el}, 输入内容: {info}")
        el.clear()
        el.send_keys(info)
        logging.info(f"输入完成: {info} 到元素: {el}")
