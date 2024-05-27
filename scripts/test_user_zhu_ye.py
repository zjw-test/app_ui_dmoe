# -*- coding: UTF-8 -*-
import logging
import time

import pytest

from common.read_json import read_json, read_json_title
from page.home_page import DemoProxy

demo_proxy = DemoProxy()


# @pytest.mark.usefixtures("demo_user_login")
class TestDemoUserHome:

    @pytest.mark.smoke
    def test_ccc(self):
        logging.info("starting test case test_ccc")
        demo_proxy.user_home_page()
        logging.info("test_ccc")
        logging.info("test case test_ccc success")

    @pytest.mark.smoke
    def test_bbb(self):
        logging.info("starting test case test_bbb")
        demo_proxy.i_home()
        logging.info("test case test_bbb success")

    @pytest.mark.smoke
    @pytest.mark.parametrize("texts", read_json("aaa.json", "aaa"),
                             ids=read_json_title("aaa.json", "aaa"))
    def test_aaa(self, texts):
        logging.info("starting test case test_aaa")
        # texts = ["测试发送消息"]
        demo_proxy.z_dan_mu(texts)
        time.sleep(60)
        logging.info("test case test_aaa success")

        # # 立即发送第一条弹幕
        # send_text = random.choice(texts)
        # demo_proxy.z_dan_mu(send_text)
        # logging.info(f"已发送弹幕: {send_text}")
        #
        # start_time = time.time()
        # end_time = start_time + 180  # 循环持续300秒
        #
        # while time.time() < end_time:
        #     time.sleep(60)  # 等待60秒
        #     send_text = random.choice(texts)  # 在循环中每次随机选择一个文本
        #     demo_proxy.z_dan_mu(send_text)
        #     logging.info(f"已发送弹幕: {send_text}")

        # logging.info("test_user_shou_ye 完成")

    # @pytest.mark.smoke
    # def test_user_zhu_ye(self):
    #     demo_proxy.user_home_page()
    #     demo_proxy.user_login()
    #     logging.info("test_user_zhu_ye")

    # @pytest.mark.smoke
    # def test_select_user(self):
    #     demo_proxy.select_user()
    #     logging.info("test_select_user")
